from django.urls import path
from tecfood_admin.views.user_view import register , login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
