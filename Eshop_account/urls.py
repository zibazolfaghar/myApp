from django.urls import path
from .views import login_user,registerـuser,log_out
urlpatterns = [
    path('login', login_user),
    path('register', registerـuser),
    path('logout', log_out),

]