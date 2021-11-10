from django.urls import path
from Product.views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('form-create/',create_form_view,name='form-create'),
    path('<int:id>/',detail_view,name='detail-view'),
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout')

]
