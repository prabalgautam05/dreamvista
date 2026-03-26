from django.db import models


class Dream(models.Model):
    text = models.TextField()
    embedding = models.JSONField()  # store vector
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
