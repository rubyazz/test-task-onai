import httpx
from celery import shared_task
from django.conf import settings

from .models import MessageHistory


@shared_task
def webhook(data):
    message = data["message"]
    callback_url = data["callback_url"]

    response_text = call_llm_api(message)

    MessageHistory.objects.create(
        message=message, response=response_text, callback_url=callback_url
    )

    async def send_callback():
        async with httpx.AsyncClient() as client:
            await client.post(callback_url, json={"response": response_text})

    send_callback()


def call_llm_api(message):
    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
    }

    try:
        response = httpx.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
        )
        response.raise_for_status()  # Raise an error for HTTP errors
        response_data = response.json()

        # Debug print
        print("Response Data:", response_data)

        return response_data["choices"][0]["message"]["content"]
    except KeyError as e:
        print(
            f"KeyError: {e} in response: {response_data}"
        )  # Log the error with response data
        return "Error: Unable to retrieve response from LLM."
    except httpx.HTTPStatusError as e:
        print(f"HTTPError: {e.response.status_code} - {e.response.text}")
        return "Error: API request failed."
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return "Error: An unexpected error occurred."
