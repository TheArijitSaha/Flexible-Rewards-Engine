from django.db import models
from datetime import datetime,timedelta,date
from django.db.models import Sum

# Create your models here.

class Scheme(models.Model):
    name                        = models.CharField(max_length=100,unique=True)
    transaction_value           = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    frequency_of_transactions   = models.IntegerField(default=0)
    vol_of_spending             = models.IntegerField(default=0)
    period                      = models.IntegerField(default=0)
    loyalty_duration            = models.IntegerField(default=0)
    valid_from                  = models.DateField(default=date.today)
    valid_to                    = models.DateField(default=date.today)

    money                       = models.IntegerField(default=0)
    points                      = models.IntegerField(default=0)

    redemp_max                  = models.IntegerField()

    def computeReward(self,value):
        if self.money==0:
            return points
        return (value//self.money)*self.points

    def is_elligible(self,transact):
        if transact.value<self.transaction_value:
            # print("Case 1")
            return False
        if transact.time_stamp<self.valid_from or transact.time_stamp>self.valid_to:
            # print("Case 2")
            return False
        if timedelta(days=self.loyalty_duration)>(date.today()-transact.user_name.date_of_issue):
            # print("Case 3")
            return False
        obj=Transaction.objects.filter(user_name=transact.user_name)
        obj=obj.filter(time_stamp__gte=date.today()-timedelta(days=self.period))
        if self.frequency_of_transactions>len(obj):
            # print("Case 4")
            return False
        if self.vol_of_spending>obj.aggregate(Sum('value'))['value__sum']:
            # print("Case 5")
            return False
        return True

    def return_rewards(self,transact):
        if self.is_elligible(transact):
            return self.computeReward(transact.value)
        else:
            return 0
