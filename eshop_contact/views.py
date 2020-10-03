from django.shortcuts import render

from eshop_setting.models import SiteSetting
from .models import ContactUs

# Create your views here.
from eshop_contact.forms import CreateContactForm


def contact_page(request):
    contact_form=CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        Email = contact_form.cleaned_data.get('Email')
        subject = contact_form.cleaned_data.get('subject')
        Text = contact_form.cleaned_data.get('Text')

        ContactUs.objects.create(full_name=full_name , Email=Email , subject=subject , Text=Text ,is_read=False)
        # todo: show user a success message
        contact_form=CreateContactForm()
    setting=SiteSetting.objects.first()

    context={
        'contact_form':contact_form,
        'setting':setting
    }
    return render(request,'contact_us/contact_us_page.html',context)
