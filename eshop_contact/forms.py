from django import forms

from django.contrib.auth.models import User
from django.core import validators


class  CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد نمایید", "class": "form-control"}),
        label='نام کاربری',
        validators=
        [
            validators.MaxLengthValidator(limit_value=150,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتراز 150 باشد'),
            validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')

        ]
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد نمایید",
                                       "class": "form-control"}),
        label='ایمیل',
        validators=

        [

            validators.MaxLengthValidator(limit_value=150,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتراز 150 باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا عنوان خود را وارد نمایید ", "class": "form-control"}),
        label='عنوان پیام',
        validators=
        [
            validators.MaxLengthValidator(limit_value=200,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتراز 200 باشد')

        ]
    )

    Text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "لطفا متن پیام خود را وارد نمایید ", 'class': "form-control", 'rows':"8"}),
        label='متن پیام'


    )