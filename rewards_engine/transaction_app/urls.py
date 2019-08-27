from django.urls import path
from transaction_app import views

app_name='transaction_app'

urlpatterns=[
    path('Create/',views.create_transaction,name='create'),
    path('List/',views.list_transaction,name='list'),
]
