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

    response = httpx.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    return response.json()["choices"][0]["message"]["content"]
