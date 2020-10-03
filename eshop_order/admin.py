from django.contrib import admin

# Register your models here.
from .models import Order,orderdetail


admin.site.register(Order)
admin.site.register(orderdetail)
