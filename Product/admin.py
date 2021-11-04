from django.contrib import admin
from .models import *
# from Product.models import Commodity
# Register your models here.

admin.site.register(Commodity)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Book)