from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from eshop_order.forms import UserNewOrderForm
from eshop_order.models import Order
from eshop_products.models import products

from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

@login_required(login_url='/login')
def add_user_order(request):
  new_order_form=UserNewOrderForm(request.POST or None)

  if new_order_form.is_valid():
      order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
      if order is None:
          order=Order.objects.create(owner_id=request.user.id,is_paid=False)
      product_id=new_order_form.cleaned_data.get('product_id')
      count = new_order_form.cleaned_data.get('count')
      if count < 0 :
          count = 1
      product = products.objects.get_by_id(product_id=product_id)
      order.orderdetail_set.create(product_id=product.id,price=product.price,count=count)
      #todo: redirect user to user panel
      #return redirect('/user')
      return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
  return redirect('/')


@login_required(login_url='/login')
def user_open_order(request):
    context={
        'order': None,
        'details':None
    }
    open_order : Order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
    if open_order is not None:
        context['order']=open_order,
        context['details']=open_order.orderdetail_set.all()

    return render(request,'order/user_open_order.html',context)



# Github.com/Rasooll


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/verify/' # Important: need to edit for realy server.

def send_request(request):
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')