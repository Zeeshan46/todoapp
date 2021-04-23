from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    created_at=models.DateField(auto_now=True)
