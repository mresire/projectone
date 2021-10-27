from django.shortcuts import render
from django.http import HttpResponse
from .models import Commodity
# Create your views here.

def home_view(request):
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
    print(id)
    product = Commodity.objects.get(id=id)
    context = {
        'commodity':product
    }
    return render(request,'detail_page.html',context)