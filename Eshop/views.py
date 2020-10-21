import itertools

from django.shortcuts import render

from eshop_products.models import products
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

def my_grouper(n, iterable):
   args = [iter(iterable)] * n
   return ([e for e in t if e is not  None] for t in itertools.zip_longest(*args))

def home_page(request):
    sliders=Slider.objects.all()
    most_visit_products=products.objects.order_by('-visit_count').all()[:4]
    latest_products=products.objects.order_by('-id').all()[:8]
    context={
        "title": "صفحه اصلی",
        'sliders': sliders,
        'most_visit': my_grouper(4,most_visit_products),
        'latest_visit': my_grouper(4,latest_products),


    }
    return render(request,'home_page.html',context)

def about_page(request):
    site_setting = SiteSetting.objects.first()
    context={
        'setting': site_setting
    }
    return render(request,'about_page.html',context)