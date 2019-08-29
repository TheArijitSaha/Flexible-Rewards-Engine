from django.shortcuts import render
from transaction_app.models import Transaction
from transaction_app.forms import TransactionCreateForm
from customer_app.models import Customer

# Create your views here.

def list_transaction(request):
    my_dict={'transact_records':Transaction.objects.order_by('time_stamp')}
    return render(request,'transaction_app/list_transact.html',context=my_dict)

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
            rewards=rewards+Customer.objects.get(name=name).current_rewards
            Customer.objects.filter(name=name).update(current_rewards=rewards)
            print(Customer.objects.get(name=name).current_rewards)
            #
            # print("FNAME: "+form.cleaned_data['first_name'])
            # print("LNAME: "+form.cleaned_data['last_name'])
            # print("EMAIL: "+form.cleaned_data['email'])
            return list_transaction(request)


    return render(request,'transaction_app/create_transaction.html',{'form':form})
