from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 500)
    isDone = models.BooleanField(default=False)
