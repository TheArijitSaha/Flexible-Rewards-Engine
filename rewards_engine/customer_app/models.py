from django.db import models
from datetime import date

# Create your models here.

class Customer(models.Model):
    name            = models.CharField(max_length=100,unique=True)
    date_of_issue   = models.DateField(default=date.today)
    cur_rewards     = models.IntegerField(default=0)
    max_red         = models.IntegerField(default=0)

    def __str__(self):
        return self.name
