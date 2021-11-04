from django import forms
from .models import *

class CommodityForm(forms.ModelForm):

    class Meta:
        model=Commodity
        fields=['name','price','description']
        
