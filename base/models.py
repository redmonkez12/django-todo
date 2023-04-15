from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    description = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"
