from django.db import models
from datetime import date
from customer_app.models import Customer
# Create your models here.

class Transaction(models.Model):
    id          = models.CharField(max_length=100,unique=True,primary_key=True)
    value       = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    time_stamp  = models.DateField(default=date.today)
    user_name   = models.ForeignKey(Customer,on_delete=models.CASCADE)
