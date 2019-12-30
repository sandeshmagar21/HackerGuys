from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName=models.CharField(max_length=120)
    CustomerAge=models.IntegerField(max_length=100)

    def __str__(self):
        return self.CustomerName
