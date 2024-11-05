from celery import shared_task
from django.conf import settings
import httpx
from .models import MessageHistory

@shared_task
def webhook(data):
    message = data["message"]
    callback_url = data["callback_url"]

    response = call_llm_api(message)
    MessageHistory.objects.create(message=message, response=response, callback_url=callback_url)

    with httpx.AsyncClient() as client:
        client.post(callback_url, json={"response": response})

def call_llm_api(message):
    return "Ответ от LLM"
