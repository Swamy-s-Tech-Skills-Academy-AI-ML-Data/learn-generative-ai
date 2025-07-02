# AI Agent API Reference

## Overview

This reference guide provides comprehensive documentation for building AI agents with various frameworks and APIs. It covers the most popular tools and libraries used in agentic AI development.

## Table of Contents

1. [LangChain Agents](#langchain-agents)
2. [AutoGen Framework](#autogen-framework)
3. [CrewAI](#crewai)
4. [OpenAI Function Calling](#openai-function-calling)
5. [Custom Agent Implementation](#custom-agent)
6. [Tool Integration](#tool-integration)
7. [Memory Systems](#memory-systems)
8. [Deployment Patterns](#deployment-patterns)

---

## LangChain Agents {#langchain-agents}

### Installation

```bash
pip install langchain langchain-openai langchain-community
```

### Basic Agent Setup

```python
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Create tools
search = DuckDuckGoSearchRun()

@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations safely."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

tools = [search, calculator]

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can search the web and perform calculations."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create agent
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute
result = agent_executor.invoke({"input": "What's the weather in New York and calculate 25 * 4?"})
print(result["output"])
```

### ReAct Agent

```python
from langchain.agents import create_react_agent

# ReAct prompt template
react_prompt = ChatPromptTemplate.from_template("""
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

# Create ReAct agent
react_agent = create_react_agent(llm, tools, react_prompt)
react_executor = AgentExecutor(agent=react_agent, tools=tools, verbose=True)
```

### Custom Tool Creation

```python
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

class EmailInput(BaseModel):
    to: str = Field(description="Email address to send to")
    subject: str = Field(description="Email subject")
    body: str = Field(description="Email body content")

class EmailTool(BaseTool):
    name = "send_email"
    description = "Send an email to a specified address"
    args_schema: Type[BaseModel] = EmailInput

    def _run(self, to: str, subject: str, body: str) -> str:
        # Implementation would connect to actual email service
        return f"Email sent to {to} with subject '{subject}'"

    async def _arun(self, to: str, subject: str, body: str) -> str:
        # Async implementation
        return self._run(to, subject, body)

# Add to tools list
email_tool = EmailTool()
tools.append(email_tool)
```

### Memory Integration

```python
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseMessage

# Create memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Agent with memory
prompt_with_memory = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with memory of our conversation."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent_with_memory = create_openai_functions_agent(llm, tools, prompt_with_memory)
agent_executor_with_memory = AgentExecutor(
    agent=agent_with_memory,
    tools=tools,
    memory=memory,
    verbose=True
)
```

---

## AutoGen Framework {#autogen-framework}

### Installation

```bash
pip install pyautogen
```

### Basic Multi-Agent Setup

```python
import autogen

# Configuration
config_list = [
    {
        "model": "gpt-4",
        "api_key": "your-api-key",
    }
]

llm_config = {
    "config_list": config_list,
    "temperature": 0,
}

# Create agents
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    system_message="A human admin who can execute code and provide feedback.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="TERMINATE",
)

assistant = autogen.AssistantAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant that can write and execute code.",
    llm_config=llm_config,
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="Write a Python script to calculate the fibonacci sequence up to n=10"
)
```

### Group Chat with Multiple Agents

```python
# Create specialized agents
coder = autogen.AssistantAgent(
    name="Coder",
    system_message="You are an expert programmer. Write clean, efficient code.",
    llm_config=llm_config,
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="You are a code reviewer. Analyze code for bugs and improvements.",
    llm_config=llm_config,
)

executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="Execute code and report results.",
    code_execution_config={"work_dir": "code_execution"},
    human_input_mode="NEVER",
)

# Create group chat
groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, critic, executor],
    messages=[],
    max_round=10,
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Start group conversation
user_proxy.initiate_chat(
    manager,
    message="Create a web scraper for extracting article titles from a news website"
)
```

### Custom Agent with Function Calling

```python
from typing import Dict, List
import json

class ResearchAgent(autogen.AssistantAgent):
    def __init__(self, name: str, **kwargs):
        super().__init__(name, **kwargs)
        self.register_function(
            function_map={
                "web_search": self._web_search,
                "save_research": self._save_research,
            }
        )

    def _web_search(self, query: str) -> str:
        """Search the web for information"""
        # Implementation would use actual search API
        return f"Search results for: {query}"

    def _save_research(self, content: str, filename: str) -> str:
        """Save research content to file"""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return f"Research saved to {filename}"
        except Exception as e:
            return f"Error saving file: {str(e)}"

# Use custom agent
research_agent = ResearchAgent(
    name="Researcher",
    system_message="You are a research assistant that can search and save information.",
    llm_config=llm_config,
)
```

---

## CrewAI {#crewai}

### Installation

```bash
pip install crewai crewai-tools
```

### Basic Crew Setup

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileReadTool

# Initialize tools
search_tool = SerperDevTool()
file_tool = FileReadTool()

# Create agents
researcher = Agent(
    role='Research Analyst',
    goal='Gather comprehensive information on given topics',
    backstory='You are an expert research analyst with years of experience in data gathering and analysis.',
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role='Content Writer',
    goal='Create engaging and informative content based on research',
    backstory='You are a skilled content writer who can transform research into compelling narratives.',
    tools=[file_tool],
    verbose=True,
    allow_delegation=False,
)

editor = Agent(
    role='Editor',
    goal='Review and improve content quality',
    backstory='You are an experienced editor with an eye for detail and quality.',
    verbose=True,
    allow_delegation=True,
)

# Create tasks
research_task = Task(
    description='Research the latest trends in artificial intelligence for 2024',
    agent=researcher,
    expected_output='A comprehensive research report with key findings and trends'
)

writing_task = Task(
    description='Write a blog post based on the research findings',
    agent=writer,
    expected_output='A well-structured blog post of 1000-1500 words',
    context=[research_task]
)

editing_task = Task(
    description='Edit and improve the blog post for clarity and engagement',
    agent=editor,
    expected_output='A polished, publication-ready blog post',
    context=[writing_task]
)

# Create crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.sequential,
    verbose=2
)

# Execute
result = crew.kickoff()
print(result)
```

### Hierarchical Process

```python
# Create crew with manager
manager = Agent(
    role='Project Manager',
    goal='Coordinate team efforts and ensure quality delivery',
    backstory='You are an experienced project manager who excels at coordinating teams.',
    allow_delegation=True,
    verbose=True,
)

hierarchical_crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.hierarchical,
    manager_agent=manager,
    verbose=2
)
```

### Custom Tools for CrewAI

```python
from crewai_tools import BaseTool
from typing import Type
from pydantic.v1 import BaseModel, Field

class DatabaseQueryInput(BaseModel):
    """Input schema for DatabaseQueryTool."""
    query: str = Field(..., description="SQL query to execute")

class DatabaseQueryTool(BaseTool):
    name: str = "Database Query"
    description: str = "Execute SQL queries against the database"
    args_schema: Type[BaseModel] = DatabaseQueryInput

    def _run(self, query: str) -> str:
        # Implementation would connect to actual database
        return f"Executed query: {query}\nResults: [sample data]"

# Use in agent
data_analyst = Agent(
    role='Data Analyst',
    goal='Analyze data and provide insights',
    backstory='You are a skilled data analyst with expertise in SQL and data interpretation.',
    tools=[DatabaseQueryTool()],
    verbose=True,
)
```

---

## OpenAI Function Calling {#openai-function-calling}

### Basic Function Calling

```python
import openai
import json
from typing import Dict, Any

def get_weather(location: str, unit: str = "celsius") -> Dict[str, Any]:
    """Get weather information for a location"""
    # Mock weather data
    return {
        "location": location,
        "temperature": 22,
        "unit": unit,
        "description": "sunny"
    }

def calculate(expression: str) -> float:
    """Safely evaluate mathematical expressions"""
    try:
        return eval(expression, {"__builtins__": {}}, {})
    except Exception as e:
        return f"Error: {str(e)}"

# Function definitions for OpenAI
functions = [
    {
        "name": "get_weather",
        "description": "Get current weather information for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and country, e.g. San Francisco, CA"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "The temperature unit"
                }
            },
            "required": ["location"]
        }
    },
    {
        "name": "calculate",
        "description": "Perform mathematical calculations",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    }
]

def execute_function_call(function_call):
    """Execute a function call"""
    function_name = function_call["name"]
    arguments = json.loads(function_call["arguments"])

    if function_name == "get_weather":
        return get_weather(**arguments)
    elif function_name == "calculate":
        return calculate(**arguments)
    else:
        return {"error": f"Unknown function: {function_name}"}

# Agent conversation with function calling
def chat_with_functions(message: str) -> str:
    messages = [{"role": "user", "content": message}]

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        function_call="auto"
    )

    message = response.choices[0].message

    if message.function_call:
        # Execute function
        function_result = execute_function_call(message.function_call)

        # Add function call and result to conversation
        messages.append({
            "role": "assistant",
            "content": None,
            "function_call": message.function_call
        })
        messages.append({
            "role": "function",
            "name": message.function_call.name,
            "content": json.dumps(function_result)
        })

        # Get final response
        final_response = openai.chat.completions.create(
            model="gpt-4",
            messages=messages
        )

        return final_response.choices[0].message.content
    else:
        return message.content

# Usage
result = chat_with_functions("What's the weather in Tokyo and what's 15 * 23?")
print(result)
```

### Advanced Function Calling Agent

```python
class FunctionCallingAgent:
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.functions = {}
        self.conversation_history = []

    def register_function(self, func, description: str, parameters: Dict[str, Any]):
        """Register a function that the agent can call"""
        self.functions[func.__name__] = {
            "function": func,
            "description": description,
            "parameters": parameters
        }

    def get_function_definitions(self) -> List[Dict[str, Any]]:
        """Get OpenAI-compatible function definitions"""
        definitions = []
        for name, info in self.functions.items():
            definitions.append({
                "name": name,
                "description": info["description"],
                "parameters": info["parameters"]
            })
        return definitions

    def execute_function(self, function_call) -> Any:
        """Execute a function call"""
        function_name = function_call["name"]
        arguments = json.loads(function_call["arguments"])

        if function_name in self.functions:
            func = self.functions[function_name]["function"]
            return func(**arguments)
        else:
            raise ValueError(f"Unknown function: {function_name}")

    def chat(self, message: str) -> str:
        """Have a conversation with function calling capabilities"""
        self.conversation_history.append({"role": "user", "content": message})

        while True:
            response = openai.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                functions=self.get_function_definitions(),
                function_call="auto"
            )

            message = response.choices[0].message

            if message.function_call:
                # Add function call to history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": None,
                    "function_call": message.function_call
                })

                # Execute function
                try:
                    result = self.execute_function(message.function_call)

                    # Add result to history
                    self.conversation_history.append({
                        "role": "function",
                        "name": message.function_call.name,
                        "content": json.dumps(result) if not isinstance(result, str) else result
                    })
                except Exception as e:
                    # Add error to history
                    self.conversation_history.append({
                        "role": "function",
                        "name": message.function_call.name,
                        "content": f"Error: {str(e)}"
                    })
            else:
                # No function call, return response
                if message.content:
                    self.conversation_history.append({
                        "role": "assistant",
                        "content": message.content
                    })
                return message.content

# Usage example
agent = FunctionCallingAgent()

# Register functions
agent.register_function(
    get_weather,
    "Get current weather for a location",
    {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City and country"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    }
)

response = agent.chat("What's the weather like in Paris?")
print(response)
```

---

## Custom Agent Implementation {#custom-agent}

### Base Agent Class

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import time
import uuid

class AgentStatus(Enum):
    IDLE = "idle"
    THINKING = "thinking"
    ACTING = "acting"
    WAITING = "waiting"
    ERROR = "error"

@dataclass
class AgentAction:
    id: str
    timestamp: float
    action_type: str
    parameters: Dict[str, Any]
    result: Any = None
    error: Optional[str] = None

@dataclass
class AgentMemory:
    short_term: List[str]
    long_term: Dict[str, Any]
    working: Dict[str, Any]

    def __post_init__(self):
        if not self.short_term:
            self.short_term = []
        if not self.long_term:
            self.long_term = {}
        if not self.working:
            self.working = {}

class BaseAgent(ABC):
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.status = AgentStatus.IDLE
        self.memory = AgentMemory([], {}, {})
        self.action_history: List[AgentAction] = []
        self.current_goal: Optional[str] = None
        self.tools: Dict[str, callable] = {}

    @abstractmethod
    def think(self, input_data: str) -> str:
        """Process input and generate reasoning"""
        pass

    @abstractmethod
    def plan(self, goal: str) -> List[Dict[str, Any]]:
        """Create a plan to achieve the goal"""
        pass

    @abstractmethod
    def act(self, action: str, parameters: Dict[str, Any]) -> Any:
        """Execute an action"""
        pass

    def register_tool(self, name: str, tool_function: callable):
        """Register a tool for the agent to use"""
        self.tools[name] = tool_function

    def set_goal(self, goal: str):
        """Set the agent's current goal"""
        self.current_goal = goal
        self.memory.working["current_goal"] = goal

    def add_to_memory(self, memory_type: str, content: Any):
        """Add information to agent memory"""
        if memory_type == "short_term":
            self.memory.short_term.append(content)
            # Keep only last 10 items in short-term memory
            if len(self.memory.short_term) > 10:
                self.memory.short_term.pop(0)
        elif memory_type == "long_term":
            key = f"memory_{int(time.time())}"
            self.memory.long_term[key] = content
        elif memory_type == "working":
            if isinstance(content, dict):
                self.memory.working.update(content)
            else:
                self.memory.working[str(uuid.uuid4())] = content

    def get_context(self) -> str:
        """Get current context for reasoning"""
        context_parts = [
            f"Current goal: {self.current_goal}",
            f"Recent memory: {self.memory.short_term[-3:] if self.memory.short_term else 'None'}",
            f"Available tools: {list(self.tools.keys())}",
            f"Current status: {self.status.value}"
        ]
        return "\n".join(context_parts)

    def log_action(self, action_type: str, parameters: Dict[str, Any], result: Any = None, error: str = None):
        """Log an action for tracking"""
        action = AgentAction(
            id=str(uuid.uuid4()),
            timestamp=time.time(),
            action_type=action_type,
            parameters=parameters,
            result=result,
            error=error
        )
        self.action_history.append(action)

        # Keep only last 50 actions
        if len(self.action_history) > 50:
            self.action_history.pop(0)
```

### Concrete Implementation

```python
class ReActAgent(BaseAgent):
    def __init__(self, name: str, llm_client, system_prompt: str = None):
        if system_prompt is None:
            system_prompt = f"You are {name}, a helpful AI agent that can reason and take actions to help users."

        super().__init__(name, system_prompt)
        self.llm_client = llm_client
        self.max_iterations = 10

    def think(self, input_data: str) -> str:
        """Generate reasoning about the current situation"""
        self.status = AgentStatus.THINKING

        context = self.get_context()
        prompt = f"""
        {self.system_prompt}

        Current Context:
        {context}

        Input: {input_data}

        Think step by step about what you need to do. Consider:
        1. What is the user asking for?
        2. What tools do you have available?
        3. What steps do you need to take?
        4. What information do you need to gather?

        Provide your reasoning:
        """

        try:
            reasoning = self.llm_client.generate(prompt)
            self.add_to_memory("short_term", f"Thought: {reasoning}")
            self.log_action("think", {"input": input_data}, reasoning)
            return reasoning
        except Exception as e:
            self.status = AgentStatus.ERROR
            self.log_action("think", {"input": input_data}, error=str(e))
            return f"Error in thinking: {str(e)}"

    def plan(self, goal: str) -> List[Dict[str, Any]]:
        """Create a detailed plan to achieve the goal"""
        self.status = AgentStatus.THINKING

        prompt = f"""
        Goal: {goal}
        Available tools: {list(self.tools.keys())}

        Create a step-by-step plan to achieve this goal. Each step should specify:
        1. The action to take
        2. The tool to use (if any)
        3. The expected outcome

        Format as a JSON list:
        [
            {{"step": 1, "action": "description", "tool": "tool_name", "expected": "outcome"}},
            ...
        ]
        """

        try:
            plan_response = self.llm_client.generate(prompt)
            # Parse JSON (simplified - in practice, use more robust parsing)
            plan = json.loads(plan_response)
            self.memory.working["current_plan"] = plan
            self.log_action("plan", {"goal": goal}, plan)
            return plan
        except Exception as e:
            self.log_action("plan", {"goal": goal}, error=str(e))
            return [{"step": 1, "action": "error", "tool": None, "expected": str(e)}]

    def act(self, action: str, parameters: Dict[str, Any]) -> Any:
        """Execute an action using available tools"""
        self.status = AgentStatus.ACTING

        try:
            if action in self.tools:
                result = self.tools[action](**parameters)
                self.add_to_memory("short_term", f"Action: {action}({parameters}) -> {result}")
                self.log_action("act", {"action": action, "parameters": parameters}, result)
                return result
            else:
                error_msg = f"Tool '{action}' not available. Available tools: {list(self.tools.keys())}"
                self.log_action("act", {"action": action, "parameters": parameters}, error=error_msg)
                return error_msg
        except Exception as e:
            error_msg = f"Error executing {action}: {str(e)}"
            self.log_action("act", {"action": action, "parameters": parameters}, error=error_msg)
            return error_msg
        finally:
            self.status = AgentStatus.IDLE

    def execute(self, user_input: str) -> str:
        """Main execution loop using ReAct pattern"""
        self.set_goal(user_input)

        for iteration in range(self.max_iterations):
            # Think about the current situation
            reasoning = self.think(user_input)

            # Check if goal is complete
            if self._is_complete(reasoning):
                return self._generate_final_response()

            # Determine next action
            action_plan = self._parse_action_from_reasoning(reasoning)

            if action_plan:
                # Execute the action
                result = self.act(action_plan["action"], action_plan["parameters"])

                # Update context with result
                user_input = f"Previous result: {result}. Continue working toward goal: {self.current_goal}"
            else:
                # No clear action, continue thinking
                user_input = f"No clear action identified. Continue analyzing the goal: {self.current_goal}"

        return "Maximum iterations reached. Goal may not be complete."

    def _is_complete(self, reasoning: str) -> bool:
        """Check if the goal appears to be complete"""
        completion_keywords = [
            "goal achieved", "task complete", "finished", "done",
            "successfully completed", "objective met"
        ]

        reasoning_lower = reasoning.lower()
        return any(keyword in reasoning_lower for keyword in completion_keywords)

    def _parse_action_from_reasoning(self, reasoning: str) -> Optional[Dict[str, Any]]:
        """Extract action and parameters from reasoning"""
        # This is a simplified parser - in practice, use more sophisticated NLP
        reasoning_lower = reasoning.lower()

        for tool_name in self.tools.keys():
            if tool_name.lower() in reasoning_lower:
                return {
                    "action": tool_name,
                    "parameters": self._extract_parameters(reasoning, tool_name)
                }

        return None

    def _extract_parameters(self, reasoning: str, tool_name: str) -> Dict[str, Any]:
        """Extract parameters for a tool from reasoning"""
        # Simplified parameter extraction
        # In practice, this would be more sophisticated
        return {}

    def _generate_final_response(self) -> str:
        """Generate final response based on action history"""
        actions_summary = []
        for action in self.action_history[-5:]:  # Last 5 actions
            if action.action_type == "act" and action.result:
                actions_summary.append(f"{action.action_type}: {action.result}")

        prompt = f"""
        Goal: {self.current_goal}
        Actions taken: {actions_summary}

        Generate a comprehensive response summarizing what was accomplished.
        """

        try:
            return self.llm_client.generate(prompt)
        except Exception as e:
            return f"Goal processing completed with some actions taken. Error in final response: {str(e)}"

# Usage example
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        # Mock implementation - replace with actual LLM client
        return "I need to search for information and then provide an answer."

# Create and use agent
agent = ReActAgent("Assistant", MockLLMClient())

# Register tools
agent.register_tool("web_search", lambda query: f"Search results for: {query}")
agent.register_tool("calculator", lambda expr: eval(expr, {"__builtins__": {}}, {}))

# Execute
result = agent.execute("What's the weather in Tokyo?")
print(result)
```

---

## Tool Integration {#tool-integration}

### Universal Tool Interface

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Type
from pydantic import BaseModel

class ToolInput(BaseModel):
    """Base class for tool inputs"""
    pass

class ToolOutput(BaseModel):
    """Base class for tool outputs"""
    success: bool
    data: Any
    error: Optional[str] = None

class BaseTool(ABC):
    """Base class for all agent tools"""

    @property
    @abstractmethod
    def name(self) -> str:
        """Tool name"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Tool description"""
        pass

    @property
    @abstractmethod
    def input_schema(self) -> Type[ToolInput]:
        """Input schema for the tool"""
        pass

    @abstractmethod
    def execute(self, input_data: ToolInput) -> ToolOutput:
        """Execute the tool"""
        pass

    def get_schema(self) -> Dict[str, Any]:
        """Get OpenAI-compatible function schema"""
        schema = self.input_schema.schema()
        return {
            "name": self.name,
            "description": self.description,
            "parameters": schema
        }

# Example tool implementations
class WebSearchInput(ToolInput):
    query: str
    num_results: int = 5

class WebSearchTool(BaseTool):
    @property
    def name(self) -> str:
        return "web_search"

    @property
    def description(self) -> str:
        return "Search the web for information"

    @property
    def input_schema(self) -> Type[ToolInput]:
        return WebSearchInput

    def execute(self, input_data: WebSearchInput) -> ToolOutput:
        try:
            # Mock implementation - replace with actual search
            results = [
                f"Result {i}: Information about {input_data.query}"
                for i in range(input_data.num_results)
            ]

            return ToolOutput(
                success=True,
                data={"results": results, "query": input_data.query}
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                data=None,
                error=str(e)
            )

class CalculatorInput(ToolInput):
    expression: str

class CalculatorTool(BaseTool):
    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Perform mathematical calculations"

    @property
    def input_schema(self) -> Type[ToolInput]:
        return CalculatorInput

    def execute(self, input_data: CalculatorInput) -> ToolOutput:
        try:
            result = eval(input_data.expression, {"__builtins__": {}}, {})
            return ToolOutput(
                success=True,
                data={"result": result, "expression": input_data.expression}
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                data=None,
                error=f"Calculation error: {str(e)}"
            )
```

### Tool Manager

```python
class ToolManager:
    """Manages tools for an agent"""

    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register_tool(self, tool: BaseTool):
        """Register a tool"""
        self.tools[tool.name] = tool

    def get_tool(self, name: str) -> Optional[BaseTool]:
        """Get a tool by name"""
        return self.tools.get(name)

    def list_tools(self) -> List[str]:
        """List all available tools"""
        return list(self.tools.keys())

    def get_schemas(self) -> List[Dict[str, Any]]:
        """Get schemas for all tools"""
        return [tool.get_schema() for tool in self.tools.values()]

    def execute_tool(self, name: str, parameters: Dict[str, Any]) -> ToolOutput:
        """Execute a tool with parameters"""
        tool = self.get_tool(name)
        if not tool:
            return ToolOutput(
                success=False,
                data=None,
                error=f"Tool '{name}' not found"
            )

        try:
            input_data = tool.input_schema(**parameters)
            return tool.execute(input_data)
        except Exception as e:
            return ToolOutput(
                success=False,
                data=None,
                error=f"Error executing tool: {str(e)}"
            )
```

---

## Memory Systems {#memory-systems}

### Hierarchical Memory

```python
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import json

@dataclass
class MemoryItem:
    content: str
    timestamp: datetime
    importance: float  # 0.0 to 1.0
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

class HierarchicalMemory:
    """Multi-level memory system for agents"""

    def __init__(self,
                 short_term_capacity: int = 20,
                 working_memory_capacity: int = 7,
                 importance_threshold: float = 0.7):
        self.short_term_capacity = short_term_capacity
        self.working_memory_capacity = working_memory_capacity
        self.importance_threshold = importance_threshold

        # Different memory stores
        self.working_memory: List[MemoryItem] = []
        self.short_term_memory: List[MemoryItem] = []
        self.long_term_memory: List[MemoryItem] = []
        self.episodic_memory: List[Dict[str, Any]] = []

    def add_memory(self, content: str, importance: float, tags: List[str] = None) -> None:
        """Add new memory item"""
        if tags is None:
            tags = []

        memory_item = MemoryItem(
            content=content,
            timestamp=datetime.now(),
            importance=importance,
            tags=tags
        )

        # Add to working memory first
        self.working_memory.append(memory_item)

        # Manage capacity and consolidation
        self._manage_working_memory()
        self._consolidate_memories()

    def _manage_working_memory(self):
        """Manage working memory capacity"""
        if len(self.working_memory) > self.working_memory_capacity:
            # Move oldest items to short-term memory
            while len(self.working_memory) > self.working_memory_capacity:
                item = self.working_memory.pop(0)
                self.short_term_memory.append(item)

    def _consolidate_memories(self):
        """Consolidate memories from short-term to long-term"""
        if len(self.short_term_memory) > self.short_term_capacity:
            # Move important items to long-term memory
            items_to_remove = []

            for i, item in enumerate(self.short_term_memory):
                if item.importance >= self.importance_threshold:
                    self.long_term_memory.append(item)
                    items_to_remove.append(i)

            # Remove consolidated items
            for i in reversed(items_to_remove):
                self.short_term_memory.pop(i)

            # Remove excess items (forgetting)
            while len(self.short_term_memory) > self.short_term_capacity:
                self.short_term_memory.pop(0)

    def retrieve_memories(self,
                         query: str,
                         max_items: int = 5,
                         memory_types: List[str] = None) -> List[MemoryItem]:
        """Retrieve relevant memories"""
        if memory_types is None:
            memory_types = ["working", "short_term", "long_term"]

        all_memories = []

        if "working" in memory_types:
            all_memories.extend(self.working_memory)
        if "short_term" in memory_types:
            all_memories.extend(self.short_term_memory)
        if "long_term" in memory_types:
            all_memories.extend(self.long_term_memory)

        # Simple relevance scoring (in practice, use vector similarity)
        relevant_memories = []
        query_words = query.lower().split()

        for memory in all_memories:
            relevance_score = 0
            content_words = memory.content.lower().split()

            # Calculate relevance
            for word in query_words:
                if word in content_words:
                    relevance_score += 1

                # Check tags
                for tag in memory.tags:
                    if word in tag.lower():
                        relevance_score += 2

            # Factor in importance and recency
            recency_bonus = 1.0 - min(1.0, (datetime.now() - memory.timestamp).days / 30)
            final_score = relevance_score * memory.importance * (1 + recency_bonus)

            if final_score > 0:
                relevant_memories.append((memory, final_score))

        # Sort by relevance and return top items
        relevant_memories.sort(key=lambda x: x[1], reverse=True)
        return [memory for memory, score in relevant_memories[:max_items]]

    def add_episode(self, episode_data: Dict[str, Any]):
        """Add episodic memory (complete interaction sequences)"""
        episode = {
            "timestamp": datetime.now().isoformat(),
            "data": episode_data,
            "summary": self._summarize_episode(episode_data)
        }
        self.episodic_memory.append(episode)

        # Keep only recent episodes
        cutoff_date = datetime.now() - timedelta(days=30)
        self.episodic_memory = [
            ep for ep in self.episodic_memory
            if datetime.fromisoformat(ep["timestamp"]) > cutoff_date
        ]

    def _summarize_episode(self, episode_data: Dict[str, Any]) -> str:
        """Create summary of an episode"""
        # Simplified summarization
        return f"Episode with {len(episode_data)} interactions"

    def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory system statistics"""
        return {
            "working_memory_size": len(self.working_memory),
            "short_term_memory_size": len(self.short_term_memory),
            "long_term_memory_size": len(self.long_term_memory),
            "episodic_memory_size": len(self.episodic_memory),
            "total_memories": (len(self.working_memory) +
                             len(self.short_term_memory) +
                             len(self.long_term_memory))
        }
```

### Vector Memory Store

```python
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Tuple, Optional

class VectorMemoryStore:
    """Vector-based memory store for semantic retrieval"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.encoder = SentenceTransformer(model_name)
        self.memories: List[MemoryItem] = []
        self.embeddings: Optional[np.ndarray] = None

    def add_memory(self, content: str, importance: float, tags: List[str] = None) -> None:
        """Add memory with semantic embedding"""
        memory_item = MemoryItem(
            content=content,
            timestamp=datetime.now(),
            importance=importance,
            tags=tags or []
        )

        self.memories.append(memory_item)

        # Update embeddings
        self._update_embeddings()

    def _update_embeddings(self):
        """Update embedding matrix"""
        if self.memories:
            contents = [memory.content for memory in self.memories]
            self.embeddings = self.encoder.encode(contents)

    def retrieve_similar(self,
                        query: str,
                        top_k: int = 5,
                        similarity_threshold: float = 0.5) -> List[Tuple[MemoryItem, float]]:
        """Retrieve semantically similar memories"""
        if not self.memories or self.embeddings is None:
            return []

        # Encode query
        query_embedding = self.encoder.encode([query])

        # Calculate similarities
        similarities = np.dot(self.embeddings, query_embedding.T).flatten()

        # Get top-k similar items above threshold
        similar_indices = np.argsort(similarities)[::-1]

        results = []
        for idx in similar_indices:
            if similarities[idx] >= similarity_threshold and len(results) < top_k:
                results.append((self.memories[idx], float(similarities[idx])))

        return results

    def cluster_memories(self, num_clusters: int = 5) -> Dict[int, List[MemoryItem]]:
        """Cluster memories by semantic similarity"""
        if not self.memories or self.embeddings is None:
            return {}

        from sklearn.cluster import KMeans

        # Perform clustering
        kmeans = KMeans(n_clusters=min(num_clusters, len(self.memories)), random_state=42)
        cluster_labels = kmeans.fit_predict(self.embeddings)

        # Group memories by cluster
        clusters = {}
        for i, label in enumerate(cluster_labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(self.memories[i])

        return clusters
```

---

## Deployment Patterns {#deployment-patterns}

### FastAPI Deployment

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import asyncio

app = FastAPI(title="AI Agent API", version="1.0.0")

class AgentRequest(BaseModel):
    agent_name: str
    message: str
    context: Dict[str, Any] = {}

class AgentResponse(BaseModel):
    success: bool
    response: str
    agent_name: str
    execution_time: float
    metadata: Dict[str, Any] = {}

# Global agent manager
agent_manager = AgentDeploymentManager()

@app.post("/agent/execute", response_model=AgentResponse)
async def execute_agent(request: AgentRequest):
    """Execute an agent request"""
    start_time = time.time()

    try:
        result = agent_manager.handle_request(request.agent_name, request.message)
        execution_time = time.time() - start_time

        return AgentResponse(
            success=result["success"],
            response=result.get("response", ""),
            agent_name=request.agent_name,
            execution_time=execution_time,
            metadata=result.get("metadata", {})
        )
    except Exception as e:
        execution_time = time.time() - start_time
        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {str(e)}"
        )

@app.get("/agent/{agent_name}/status")
async def get_agent_status(agent_name: str):
    """Get agent status and metrics"""
    return agent_manager.get_performance_report(agent_name)

@app.post("/agent/{agent_name}/deploy")
async def deploy_agent(agent_name: str, config: Dict[str, Any]):
    """Deploy a new agent"""
    # Implementation depends on your agent creation logic
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-agent-api
  labels:
    app: ai-agent-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-agent-api
  template:
    metadata:
      labels:
        app: ai-agent-api
    spec:
      containers:
        - name: ai-agent-api
          image: your-registry/ai-agent-api:latest
          ports:
            - containerPort: 8000
          env:
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: openai-api-key
          resources:
            requests:
              memory: "512Mi"
              cpu: "250m"
            limits:
              memory: "1Gi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 5

---
apiVersion: v1
kind: Service
metadata:
  name: ai-agent-service
spec:
  selector:
    app: ai-agent-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: LoadBalancer
```

This comprehensive API reference provides you with the tools and patterns needed to build sophisticated AI agents. Each framework has its strengths:

- **LangChain**: Rich ecosystem and easy tool integration
- **AutoGen**: Excellent for multi-agent conversations
- **CrewAI**: Business process focused with role-based agents
- **OpenAI Function Calling**: Direct integration with OpenAI models
- **Custom Implementation**: Full control and flexibility

Choose the approach that best fits your specific use case and requirements.

---

_This API reference is part of the learn-generative-ai repository's comprehensive guide to AI agent development._
