from django.urls import path

from eshop_order.views import add_user_order, user_open_order, send_request, verify

urlpatterns = [
  path('add-user-order',add_user_order),
  path('open-order',user_open_order),
  path('request', send_request, name='request'),
  path('verify', verify , name='verify'),
]

