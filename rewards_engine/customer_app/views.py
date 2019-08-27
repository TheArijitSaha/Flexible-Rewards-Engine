from django.shortcuts import render
from customer_app.forms import CustomerCreateForm
from customer_app.models import Customer

# Create your views here.

def list_customer(request):
    my_dict={'cust_records':Customer.objects.order_by('name')}
    return render(request,'customer_app/list_customer.html',context=my_dict)

def create_customer(request):
    form=CustomerCreateForm()

    if request.method=='POST':
        form=CustomerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("VALIDATION SUCCESSFUL")
            return list_customer(request)


    return render(request,'customer_app/create_customer.html',{'form':form})
