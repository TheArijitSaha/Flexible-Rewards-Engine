from django.urls import path
from scheme_app import views

app_name='scheme_app'

urlpatterns=[
    path('List/',views.list_scheme,name='list'),
    path('Create/',views.create_scheme,name='create'),
]
