
from django.shortcuts import render
from eshop_slider.models import Slider
from eshop_setting.models import SiteSetting

def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)
def footer(request, *args, **kwargs):
    site_setting=SiteSetting.objects.first()
    context = {
            'setting': site_setting

    }

    return render(request, 'shared/Footer.html', context)

def home_page(request):
    sliders=Slider.objects.all()
    context={
        "title": "صفحه اصلی",
        'sliders': sliders

    }
    return render(request,'home_page.html',context)

def about_page(request):
    site_setting = SiteSetting.objects.first()
    context={
        'setting': site_setting
    }
    return render(request,'about_page.html',context)