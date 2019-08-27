from django.shortcuts import render
from scheme_gen.forms import SchemeCreateForm,TransactionCreateForm,CustomerCreateForm
from scheme_gen.models import Scheme,Transaction,Customer

# Create your views here.

def index(request):
    return render(request,'scheme_gen/index.html')

def list_scheme(request):
    my_dict={'scheme_records':Scheme.objects.order_by('name')}
    return render(request,'scheme_gen/list_scheme.html',context=my_dict)

def list_customer(request):
    my_dict={'cust_records':Customer.objects.order_by('name')}
    return render(request,'scheme_gen/list_customer.html',context=my_dict)

def create_scheme(request):
    form=SchemeCreateForm()

    if request.method=='POST':
        form=SchemeCreateForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESSFUL")
            # print("FNAME: "+form.cleaned_data['first_name'])
            # print("LNAME: "+form.cleaned_data['last_name'])
            # print("EMAIL: "+form.cleaned_data['email'])
            form.save()
            return list_scheme(request)


    return render(request,'scheme_gen/create_scheme.html',{'form':form})
def create_customer(request):
    form=CustomerCreateForm()

    if request.method=='POST':
        form=CustomerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("VALIDATION SUCCESSFUL")
            return list_customer(request)


    return render(request,'scheme_gen/create_customer.html',{'form':form})

def list_transaction(request):
    my_dict={'transact_records':Transaction.objects.order_by('time_stamp')}
    return render(request,'scheme_gen/list_transact.html',context=my_dict)

def create_transaction(request):
    form=TransactionCreateForm()

    if request.method=='POST':
        form=TransactionCreateForm(request.POST)
        if form.is_valid():
            m=form.save()
            print("VALIDATION SUCCESSFUL")
            rewards=0
            for entry in Scheme.objects.all():
                rewards= max(rewards, entry.return_rewards(m))
            print("Rewards earned: "+str(rewards))
            name = m.user_name
            rewards=rewards+Customer.objects.get(name=name).cur_rewards
            Customer.objects.filter(name=name).update(cur_rewards=rewards)
            print(Customer.objects.get(name=name).cur_rewards)
            #
            # print("FNAME: "+form.cleaned_data['first_name'])
            # print("LNAME: "+form.cleaned_data['last_name'])
            # print("EMAIL: "+form.cleaned_data['email'])
            return list_transaction(request)


    return render(request,'scheme_gen/create_transaction.html',{'form':form})
