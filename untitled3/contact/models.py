from django.db import models

# Create your models here.
class Query(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.EmailField()
    content=models.TextField()

    def __str__(self):
        return self.email



