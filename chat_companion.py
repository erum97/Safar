# chat_companion.py
from groq import Groq

from config import (
    GROQ_API_KEY,
    GROQ_MODEL,
    MAX_HISTORY_MESSAGES,
    MAX_TOKENS,
    TEMPERATURE,
)
from prompts import build_system_prompt


def get_groq_client():
    """Create a Groq client using the API key."""

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to your .env file "
            "or Streamlit Cloud Secrets."
        )

    return Groq(api_key=GROQ_API_KEY)


def get_ai_response(
    user_message: str,
    chat_history: list,
    trip_data: dict,
) -> str:
    """
    Send the user message, chat history, and trip data to Groq.
    """

    if not user_message or not user_message.strip():
        return "Please enter a question before sending your message."

    try:
        client = get_groq_client()

        messages = [
            {
                "role": "system",
                "content": build_system_prompt(trip_data),
            }
        ]

        # Keep only the latest messages to reduce token usage.
        recent_history = chat_history[-MAX_HISTORY_MESSAGES:]

        for message in recent_history:
            role = message.get("role")
            content = message.get("content")

            if role in ["user", "assistant"] and content:
                messages.append(
                    {
                        "role": role,
                        "content": content,
                    }
                )

        messages.append(
            {
                "role": "user",
                "content": user_message.strip(),
            }
        )

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )

        answer = response.choices[0].message.content

        if not answer:
            return "I could not generate a response. Please try again."

        return answer.strip()

    except ValueError as error:
        return f"Configuration error: {error}"

    except Exception as error:
        error_message = str(error).lower()

        if (
            "authentication" in error_message
            or "api key" in error_message
            or "unauthorized" in error_message
        ):
            return (
                "Your Groq API key is invalid or unavailable. "
                "Please check your API key configuration."
            )

        if (
            "model" in error_message
            and (
                "not found" in error_message
                or "decommissioned" in error_message
            )
        ):
            return (
                f"The model '{GROQ_MODEL}' is unavailable. "
                "Please check the model name in your Groq Console."
            )

        if (
            "rate limit" in error_message
            or "429" in error_message
            or "too many requests" in error_message
        ):
            return (
                "The free Groq usage limit has temporarily been reached. "
                "Please wait and try again later."
            )

        return (
            "I could not connect to Groq right now. "
            "Please check your internet connection and try again."
        )
