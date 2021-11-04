from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Commodity
from .forms import *
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