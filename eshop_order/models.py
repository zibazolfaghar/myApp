from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import products

# Create your models here.

class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField( verbose_name='پرداخت شده / نشده')
    payment_date = models.DateField(blank=True,null=True,verbose_name='تاریخ پرداختی')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):

        return self.owner.get_full_name()

class orderdetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='سبد خرید')
    product = models.ForeignKey(products, on_delete=models.CASCADE,verbose_name='محصول')
    price=models.IntegerField(verbose_name='قیمت محصول')
    count=models.IntegerField(verbose_name='تعداد محصول')

    def get_detail_sum(self):
        return self.count * self.price
    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصول'

    def __str__(self):

        return self.product.title




