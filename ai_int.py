import json
import os

import requests
from dotenv import load_dotenv
from config import BOT_REP


# Load variables from .env so the API key is not hardcoded in the script.
load_dotenv()

# OpenRouter needs your API key before sending any chat request.
# If the key is missing, the bot should stop immediately.
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise SystemExit(
        "Missing OPENROUTER_API_KEY.\n"
    )


# These headers are required by the OpenRouter API for authentication and metadata.
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://example.com",
    "X-Title": "Say my name to use the ai",
}


# This is a backup list. If the first model is busy, the code tries another one.
# some models may be rate-limited or unavailable, so check that the model you want to use is available on OpenRouter.
FALLBACK_MODELS = [
    "inclusionai/ling-3.0-flash-fin:free",
<<<<<<< HEAD
    "poolside/laguna-s-2.1:free",

=======
    "inclusionai/ling-3.0-flash-sante:free",
    "nex-agi/nex-n2.5-pro:free",
    "dots-studio/dots-3-note-preview:free",
    "thinkingmachines/inkling-small:free",
    "poolside/laguna-xs-2.1:free",
    "liquid/lfm-2.5-2.6b:free",
    
>>>>>>> 0278fb53861dceb4f5ec3c6bf5d808f23ddd7d9c
]



# if the AI service says "error", this function makes the error easy to read.

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

# This function sends a request to OpenRouter and handles errors.
def call_openrouter(payload, fallback_models=None):
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


# Real magic happens here. This function builds the request payload for OpenRouter.
def build_payload(raw_input):
    system_message = {"role": "system", "content": BOT_REP}
    user_text = normalize_input(raw_input)
    user_message = {"role": "user", "content": user_text}

    return {
        "model": "inclusionai/ling-3.0-flash-fin:free",
        "messages": [system_message, user_message],
        "reasoning": {"enabled": True},
    }


def main(raw_input):
    """
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
    


