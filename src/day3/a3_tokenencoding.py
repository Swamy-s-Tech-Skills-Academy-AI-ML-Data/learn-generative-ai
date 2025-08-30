# **Python Helper Function**
import tiktoken


def get_encoding_for_model(model_name: str) -> tiktoken.Encoding:
    """  
    Determine and return the correct tiktoken encoding for a given OpenAI model.  

    This function uses tiktoken's internal mapping to look up the correct  
    encoding scheme for the specified model. Encodings define how text is  
    split into tokens and how tokens are mapped to unique IDs.  

    If the provided model name is not recognized, the function falls back  
    to using 'cl100k_base', which is the default encoding for most modern  
    OpenAI models (e.g., GPT-4, GPT-3.5, and latest embeddings).  

    Args:  
        model_name (str):  
            The name of the OpenAI model (e.g., "gpt-4", "text-davinci-003").  
            The name should match an official OpenAI model identifier.  

    Returns:  
        tiktoken.Encoding:  
            The encoding object corresponding to the given model. This object  
            can be used to encode text into token IDs and decode token IDs back  
            into text.  

    Example:  
        >>> enc = get_encoding_for_model("gpt-4")  
        >>> tokens = enc.encode("Hello world!")  
        >>> print(tokens)  
        [9906, 1917, 0]  
        >>> text = enc.decode(tokens)  
        >>> print(text)  
        Hello world!  
    """
    try:
        # tiktoken has a built-in function for this lookup
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        # If the model isn't recognized, use cl100k_base as a safe default
        print(
            f"[Warning] Model '{model_name}' not found in tiktoken database. Using 'cl100k_base'.")
        encoding = tiktoken.get_encoding("cl100k_base")
    return encoding


# Example usage
if __name__ == "__main__":
    models = [
        "gpt-4",
        "gpt-3.5-turbo",
        "text-davinci-003",
        "code-davinci-002",
        "davinci",
        "text-embedding-ada-002",
        "unknown-model"
    ]

    for model in models:
        enc = get_encoding_for_model(model)
        print(f"Model: {model:<25} | Encoding: {enc.name}")

# # **Example Output**
# ```
# Model: gpt-4 | Encoding: cl100k_base
# Model: gpt-3.5-turbo | Encoding: cl100k_base
# Model: text-davinci-003 | Encoding: p50k_base
# Model: code-davinci-002 | Encoding: p50k_base
# Model: davinci | Encoding: r50k_base
# Model: text-embedding-ada-002 | Encoding: cl100k_base
# [Warning] Model 'unknown-model' not found in tiktoken database. Using 'cl100k_base'.
# Model: unknown-model | Encoding: cl100k_base
