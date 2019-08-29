from django.db import models
from datetime import date

# Create your models here.

class Customer(models.Model):
    customer_id         = models.IntegerField(default=0,unique=True,primary_key=True)
    name                = models.CharField(max_length=100)
    date_of_creation    = models.DateField(default=date.today)
    current_rewards     = models.IntegerField(default=0)

    def __str__(self):
        return self.name
