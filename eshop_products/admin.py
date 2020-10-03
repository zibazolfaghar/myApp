from django.contrib import admin

# Register your models here.
from .models import products
from .models import productsgallery

class ProductAdmin(admin.ModelAdmin):
  list_display = ['__str__','title','price','description','active']
  class Meta:
        model=products

admin.site.register(products,ProductAdmin)
admin.site.register(productsgallery)