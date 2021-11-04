from django.urls import path
from Product.views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('form-create/',create_form_view,name='form-create'),
    path('<int:id>/',detail_view,name='detail-view')
]
