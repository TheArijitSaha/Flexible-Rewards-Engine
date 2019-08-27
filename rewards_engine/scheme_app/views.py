from django.shortcuts import render
from scheme_app.forms import SchemeCreateForm
from scheme_app.models import Scheme

# Create your views here.

def index(request):
    return render(request,'base.html')

def list_scheme(request):
    my_dict={'scheme_records':Scheme.objects.order_by('name')}
    return render(request,'scheme_app/list_scheme.html',context=my_dict)

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

    return render(request,'scheme_app/create_scheme.html',{'form':form})
