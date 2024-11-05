from django.db import models

class MessageHistory(models.Model):
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    callback_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message