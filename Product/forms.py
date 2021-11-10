from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommodityForm(forms.ModelForm):

    class Meta:
        model=Commodity
        fields=['name','price','description']


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']


        
