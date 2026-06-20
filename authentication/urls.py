from django.urls import path
from .views import *

urlpatterns = [
    path('', loginpage, name='loginpage'),
    path('logout/', logoutpage, name='logoutpage'),
    path('signup/', signuppage, name='signuppage'),
]