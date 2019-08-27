from django.urls import path
from customer_app import views

app_name='customer_app'

urlpatterns=[
    path('Create/',views.create_customer,name='create'),
    path('List/',views.list_customer,name='list'),
]
