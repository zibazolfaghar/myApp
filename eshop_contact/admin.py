from django.contrib import admin

# Register your models here.
from .models import ContactUs


class Contactus(admin.ModelAdmin):
  list_display = ['__str__','full_name','Email','subject','Text','is_read']
  list_filter = ['is_read']
  list_editable = ['is_read','subject']
  search_fields = ['subject']


  class Meta:
        model=ContactUs

admin.site.register(ContactUs,Contactus)

