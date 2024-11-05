from rest_framework import serializers

class WebhookSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=5000)
    callback_url = serializers.URLField()

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value
