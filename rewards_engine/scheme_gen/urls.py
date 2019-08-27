from django.urls import path
from scheme_gen import views

app_name='scheme_gen'
urlpatterns=[
    path('List/',views.list_scheme,name='list'),
    path('Create/',views.create_scheme,name='create'),
    path('create_transaction/',views.create_transaction,name='formcreate'),
    path('list_transaction/',views.list_transaction,name='formlist'),
    path('list_customer/',views.list_customer,name='customerlist'),
    path('create_customer/',views.create_customer,name='customerform'),
]
