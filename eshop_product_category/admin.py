
from django.contrib import admin

# Register your models here.
from eshop_product_category.models import productcategory

class Productcategoryadmin(admin.ModelAdmin):
  list_display = ['__str__','name']


  class Meta:
        model=productcategory

admin.site.register(productcategory,Productcategoryadmin)



