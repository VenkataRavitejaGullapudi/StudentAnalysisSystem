from django.db import models

# Create your models here.
class Faqs(models.Model):
    email=models.EmailField()
    query=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000,default=" none ")
    def __str__(self):
        return self.query
