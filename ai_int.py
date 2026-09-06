import json
import os

import requests
from dotenv import load_dotenv
from config import BOT_REP

# ============================================================
# Beginner guide for this file
# ============================================================
# This file connects your Telegram bot to an AI model from OpenRouter.
# In simple words:
#   1. it reads the AI key
#   2. prepares the message to send
#   3. sends it to the online AI service
#   4. gets the answer back
#   5. returns the answer to the bot so Telegram can show it
#
# Think of it like this:
#   - Telegram sends a message
#   - this file turns it into a clean text question
#   - OpenRouter answers the question
#   - the answer goes back to the user
# ============================================================

# Load variables from .env so the API key is not hardcoded in the script.
load_dotenv()

# OpenRouter needs your API key before sending any chat request.
# If the key is missing, the bot should stop immediately.
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise SystemExit(
        "Missing OPENROUTER_API_KEY.\n"
        "Set it first in config.py."
    )

# AI_REPRESENTATIVE is the system prompt.
# It tells the AI how it should behave or speak.
AI_REPRESENTATIVE = BOT_REP

# These headers are required by the OpenRouter API for authentication and metadata.
# They are like ID cards showing who is making the request.
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://example.com",
    "X-Title": "Say my name to use the ai",
}

# If the free model is rate-limited or temporarily unavailable,
# try another model instead of crashing on the first 429 response.
# This is a backup list. If the first model is busy, the code tries another one.
FALLBACK_MODELS = [
    "minimax/minimax-m3:free",
    "google/gemma-4-31b-it:free",
    "minimax/minimax-m2.7:free",
    "poolside/laguna-s-2.1:free",
]


# OpenRouter sometimes returns an error object instead of a normal completion payload.
# This helper turns that into a readable message.
# In simple words: if the AI service says "error", this function makes the error easy to read.
def extract_error_message(data):
    """
    Convert an OpenRouter error response into a simple text message.
    This makes debugging much easier for beginners.
    """
    if not isinstance(data, dict):
        return None

    error = data.get("error")
    if not isinstance(error, dict):
        return None

    message = error.get("message", "Unknown OpenRouter error")
    code = error.get("code")
    if code:
        return f"OpenRouter API error ({code}): {message}"
    return f"OpenRouter API error: {message}"


def call_openrouter(payload, fallback_models=None):
    """
    Send the request to OpenRouter and retry with fallback models if needed.

    Why this matters:
    - Some AI models may be busy or rate-limited.
    - This function tries the first model, then backups if needed.

    In beginner terms:
    - payload = the question we want to send
    - models = list of AI models to try
    - if one model fails, try the next one
    """
    models = []
    primary_model = payload.get("model")
    if primary_model:
        models.append(primary_model)
    models.extend(fallback_models or [])
    models = list(dict.fromkeys(models))

    last_error = None
    for model in models:
        attempt_payload = dict(payload)
        attempt_payload["model"] = model
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=attempt_payload,
                timeout=(10, 120),
            )
            data = response.json()
        except requests.exceptions.Timeout:
            raise SystemExit("OpenRouter request timed out after 120s while waiting for a response.")
        except requests.exceptions.RequestException as exc:
            response = getattr(exc, "response", None)
            if response is not None:
                try:
                    data = response.json()
                except ValueError:
                    data = {"error": {"message": str(exc), "code": getattr(response, "status_code", "unknown")}}
            else:
                raise SystemExit(f"OpenRouter request failed: {exc}")
        else:
            if response.status_code >= 400:
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError:
                    error_message = extract_error_message(data) or f"OpenRouter request failed with status {response.status_code}."
                    if response.status_code == 429 and model != models[-1]:
                        last_error = error_message
                        continue
                    raise SystemExit(error_message)

        error_message = extract_error_message(data)
        if error_message:
            if response.status_code == 429 and model != models[-1]:
                last_error = error_message
                continue
            raise SystemExit(error_message)

        if "choices" not in data:
            raise KeyError(f"OpenRouter response did not include 'choices': {data}")

        return data

    if last_error:
        raise SystemExit(f"All fallback models were rate-limited. Last error: {last_error}")
    raise SystemExit("OpenRouter request failed without a usable response from any model.")



def normalize_input(value):
    """
    Make sure the AI always receives plain text.

    Telegram sends a Message object, but OpenRouter wants a normal string.
    This function pulls the message text out safely.

    Beginner explanation:
    - if the input is already text, keep it
    - if it is a Telegram message object, read its .text field
    - if it is empty, return an empty string
    """
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if hasattr(value, "text"):
        text = getattr(value, "text")
        if text is None:
            return ""
        return text
    return str(value)


def build_payload(raw_input):
    """
    Build the JSON body that OpenRouter expects.

    This is the exact format the AI API understands:
    - model: which AI model to use
    - messages: conversation history
    - reasoning: if we want the model to explain its thinking

    Beginner explanation:
    We are making a structured message package for the AI.
    The AI needs a role and content for each message.
    """
    system_message = {"role": "system", "content": AI_REPRESENTATIVE}
    user_text = normalize_input(raw_input)
    user_message = {"role": "user", "content": user_text}

    return {
        "model": "google/gemma-4-31b-it:free",
        "messages": [system_message, user_message],
        "reasoning": {"enabled": True},
    }


def main(raw_input):
    """
    Main AI entry point.

    1. Convert Telegram message into plain text
    2. Build the request payload
    3. Send it to OpenRouter
    4. Read the AI response and return it

    Beginner explanation:
    This is the main engine of the bot.
    It receives the user's message, asks the AI for help,
    and then gives the AI answer back to Telegram.
    """
    first_payload = build_payload(raw_input)

    first_data = call_openrouter(first_payload, fallback_models=FALLBACK_MODELS)

    # Extract the assistant message from the API response.
    message = first_data["choices"][0]["message"]

    # Print the full first response and the answer to the follow-up question.
    print("\n")
    print(f"\n{message.get('reasoning_details', '')}\n")
    print(message["content"])

    return message.get("reasoning_details", ""), message["content"]
    


