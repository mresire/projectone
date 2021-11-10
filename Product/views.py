from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Commodity
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home_view(request):

    # print(request.user)
    user = request.user
    user_data = Commodity.objects.all()
    print(user_data)
    data = {
        'name':user,
        'products':user_data
    }
    return render(request,'home.html',data)

def abc_view(request):
    return HttpResponse('<h3>ABC</h3>')

def detail_view(request,id):
    # product = Commodity.objects.get(id=id)
    # try:
    #     product = Commodity.objects.get(id=id)
    # except Commodity.DoesNotExist:
    #     raise Http404
    product = get_object_or_404(Commodity,pk=id)
    

    context = {
        'commodity':product
    }
    return render(request,'detail_page.html',context)


def create_form_view(request):
    # print(request.GET)
    # print(request.POST)
    form = CommodityForm(request.POST or None)
    # print(f"{form}")

    if form.is_valid():
        data=form.cleaned_data
        # print(data['name'])
        # print(data.get('description'))
        # Commodity.objects.create(**data)
        form.save()
        form = CommodityForm()

    context = {
        'form':form
        }


    return render(request,'commodity_create.html',context)

def register(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()


    context = {'form':form}

    return render(request,'registration/register.html',context)


def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')

            
    context = {}

    return render(request,'registration/login.html')

def logout_view(request):
    logout(request)

    return redirect('login')