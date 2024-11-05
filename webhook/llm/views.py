from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WebhookSerializer
from .tasks import webhook

class WebhookView(APIView):
    def post(self, request):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            webhook.delay(serializer.data)
            return Response({"message": "Processing started"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
