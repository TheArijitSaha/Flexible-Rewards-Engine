import os
from datetime import datetime,timedelta,date

os.environ.setdefault("DJANGO_SETTINGS_MODULE","hack_proj.settings")

import django
django.setup()

import random
from scheme_gen.models import Customer,Scheme
from faker import Faker

fakegen=Faker()

def clear_all():
    Customer.objects.all().delete()
    Scheme.objects.all().delete()


def populate():
    Customer.objects.get_or_create(name='Cust1',date_of_issue=date.today(),cur_rewards=0,max_red=1000000)
    Customer.objects.get_or_create(name='Cust2',date_of_issue=date.today()-timedelta(days=720),cur_rewards=0,max_red=1000000)
    Customer.objects.get_or_create(name='Cust3',date_of_issue=date.today()-timedelta(days=(5*365)),cur_rewards=0,max_red=1000000)

if __name__=="__main__":
    populate()
    # clear_all()
