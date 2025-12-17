from openai import OpenAI


def chat_completion(
    client: OpenAI,
    model_name: str,
    prompt: str,
    max_tokens: int | None = None,
    temperature: float | None = None,
    response_format: dict | None = None,
) -> str:
    # Build request parameters
    request_params = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
    }

    # Add optional parameters if provided
    if max_tokens is not None:
        request_params["max_tokens"] = max_tokens
    if temperature is not None:
        request_params["temperature"] = temperature

    # Add response_format if provided (for structured output / JSON mode)
    if response_format:
        request_params["response_format"] = response_format

    response = client.chat.completions.create(**request_params)

    content = response.choices[0].message.content
    if content is None:
        raise ValueError("Chat completion returned None content")
    return content
