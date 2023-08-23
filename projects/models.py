from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)