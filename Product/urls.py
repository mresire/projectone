from django.urls import path
from Product.views import home_view,detail_view,abc_view

urlpatterns = [
    path('',home_view,name='home'),
    # path('abc/',abc_view,name='abc'),
    path('<int:id>/',detail_view,name='detail-view')
]
