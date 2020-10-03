from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.models import User

def login_user(request):
    if request.user.is_authenticated:
        return  redirect('/')
    login_form=LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name','کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form':login_form

    }
    return render(request,'account\login.html',context)


def registerـuser(request):
    if request.user.is_authenticated:
        return  redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get("user_name")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")
        User.objects.create_user( username=user_name, password=password,email=email)
        return redirect('/login')
    context = {

        'register_form': register_form

    }
    return render(request, 'account\Register.html', context)
def log_out(request):
    logout(request)
    return redirect('/login')