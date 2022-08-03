from django.urls import path
from .views import *

app_name = 'facebook'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup')
]

