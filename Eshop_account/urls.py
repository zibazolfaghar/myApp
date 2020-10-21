from django.urls import path
from .views import login_user, registerـuser, log_out, user_account_main_page,edit_user_profile

urlpatterns = [
    path('login', login_user),
    path('register', registerـuser),
    path('logout', log_out),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),

]