import os
import requests


def generate_gemini_response(prompt):
    """
    Sends a prompt to Google Gemini API.
    Returns generated text.
    """

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    if not api_key:
        return (
            "Gemini API key is not configured. "
            "PocketSmart AI is currently running in demo mode."
        )

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={api_key}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        candidates = data.get("candidates", [])

        if not candidates:
            return "Gemini did not return a recommendation."

        parts = candidates[0].get("content", {}).get("parts", [])

        result = ""

        for part in parts:
            if "text" in part:
                result += part["text"]

        return result.strip()

    except requests.exceptions.RequestException as error:
        return f"Gemini API error: {error}"

    except Exception as error:
        return f"Unexpected AI error: {error}"