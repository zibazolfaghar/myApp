from django import forms
from django.contrib.auth.models import User
from django.core import validators

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={ "placeholder": "لطفا نام کاربری خود را وارد نمایید"}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={ "placeholder": "لطفا کلمه عبور خود را وارد نمایید "}),
        label = 'کلمه عبور'
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist_user=User.objects.filter(username=user_name).exists()
        if not is_exist_user:
            raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')

        return user_name

class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={ "placeholder": "لطفا نام کاربری خود را وارد نمایید"}),
        label='نام کاربری',
        validators=
        [
            validators.MaxLengthValidator(limit_value=20,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتراز 20 باشد'),
            validators.MinLengthValidator(8,'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')

        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد نمایید "}),
        label='ایمیل',
        validators =

        [
             validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={ "placeholder": "لطفا کلمه عبور خود را وارد نمایید "}),
        label = 'کلمه عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا تکرار کلمه عبور خود را وارد نمایید "}),
        label='تکرار کلمه عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist_email = User.objects.filter(email=email).exists()
        if is_exist_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist_user=User.objects.filter(username=user_name).exists()
        if  is_exist_user:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return user_name

        return user_name
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور با هم مغایرت دارند')
        return password