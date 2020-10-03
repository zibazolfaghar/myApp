
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


from Eshop import settings
from .views import home_page,header,footer,about_page

urlpatterns = [
    path('', home_page),
    path('about_us', about_page),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('', include('Eshop_account.urls')),
    path('', include('eshop_products.urls')),
    path('', include('eshop_contact.urls')),
    path('', include('eshop_order.urls')),
    path('admin/', admin.site.urls)
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)