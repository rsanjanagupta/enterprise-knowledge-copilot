import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(prompt):
    payload = {
        "model": "phi",      # 🔥 use phi for speed
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()
        return response.json()["response"]

    except requests.exceptions.Timeout:
        return "LLM timed out."

    except requests.exceptions.RequestException as e:
        return f"LLM error: {e}"
