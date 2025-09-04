r"""Extract contact details from free-form text using the OpenAI API.

Fields extracted:
- first_name
- company
- location
- email
- phone

Requirements:
- Set OPENAI_API_KEY in your environment (or .env)
- pip install openai

Usage (PowerShell):
  # with built-in sample
  py .\src\day2\extract_contact_info_openai.py

  # with a text file
  py .\src\day2\extract_contact_info_openai.py .\path\to\file.txt

Optional environment variables:
- OPENAI_MODEL   (default: gpt-3.5-turbo)
"""

from __future__ import annotations

import json
import os
import sys
import importlib
from pathlib import Path
from typing import Any, Dict

# Optional .env support if python-dotenv is available
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(
            "Missing OPENAI_API_KEY. Set it in your environment or in a .env file.\n"
            "PowerShell (current session):  $env:OPENAI_API_KEY=\"<your-key>\"\n"
            "Create .env in repo root:     OPENAI_API_KEY=<your-key>",
            file=sys.stderr,
        )
        raise SystemExit(1)

    try:
        openai_module = importlib.import_module("openai")
        OpenAI = getattr(openai_module, "OpenAI")
    except Exception:
        print(
            "Missing dependency: openai. Install with:\n  pip install openai",
            file=sys.stderr,
        )
        raise SystemExit(1)

    return OpenAI(api_key=api_key)


SYSTEM_PROMPT = (
    "You are a precise information extraction assistant. "
    "Extract contact information from the user's message and return ONLY a JSON object with these keys: "
    "first_name, company, location, email, phone. Use null for any missing value. "
    "Do not add extra keys or commentary. No markdown fences."
)

USER_INSTRUCTION = (
    "From the following text, extract: first_name, company, location, email, phone. "
    "Return a compact JSON object with exactly those keys."
)

SAMPLE_TEXT = (
    "Hi there. I'm Priya Sharma from Contoso Health, Austin, TX. "
    "I heard you're exploring our employee wellness packages. "
    "When you have a moment, please call me at 425-555-0139 so we can review options. "
    "I'm available Monday to Friday during normal business hours Central Time. "
    "You can also reach me by email at priya.sharma@contosohealth.com. "
    "Thanks, Priya."
)


def call_openai_extract(client: Any, text: str, model: str) -> Dict[str, Any]:
    """Call OpenAI to extract fields.

    Tries JSON response_format first (for models that support it, e.g., gpt-4o, gpt-4o-mini).
    If the model rejects response_format (e.g., classic gpt-4), retries without it using
    strict instructions to return raw JSON.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"{USER_INSTRUCTION}\n\nText:\n{text}"},
    ]

    def _parse_content_to_json(content: str) -> Dict[str, Any]:
        try:
            return json.loads(content)
        except Exception:
            start = content.find("{")
            end = content.rfind("}")
            if start != -1 and end != -1 and end > start:
                return json.loads(content[start: end + 1])
            raise RuntimeError("Model did not return valid JSON content")

    # Use response_format only for models that support it (e.g., gpt-4o family)
    def _supports_json_object(m: str) -> bool:
        ml = m.lower()
        return ml.startswith("gpt-4o")

    if _supports_json_object(model):
        try:
            resp = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=messages,
                temperature=0.0,
            )
            content = resp.choices[0].message.content
            data = _parse_content_to_json(content)
        except Exception as e:
            # Fallback: retry without response_format if not supported
            err_text = f"{e}".lower()
            if "response_format" in err_text or "invalid parameter" in err_text:
                resp = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=0.0,
                )
                content = resp.choices[0].message.content
                data = _parse_content_to_json(content)
            else:
                raise
    else:
        # Directly call without response_format for models like gpt-4 / gpt-3.5
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.0,
        )
        content = resp.choices[0].message.content
        data = _parse_content_to_json(content)

    # Ensure required keys exist, fill with None if missing
    result = {
        "first_name": data.get("first_name"),
        "company": data.get("company"),
        "location": data.get("location"),
        "email": data.get("email"),
        "phone": data.get("phone"),
    }
    return result


def _load_text_from_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def main(argv: list[str]) -> int:
    model = os.getenv("OPENAI_MODEL", "gpt-4")
    client = get_openai_client()

    if len(argv) > 1:
        path = Path(argv[1])
        if not path.exists():
            print(f"Input file not found: {path}", file=sys.stderr)
            return 2
        text = _load_text_from_file(path)
    else:
        text = SAMPLE_TEXT

    result = call_openai_extract(client, text, model)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
