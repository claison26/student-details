
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('show/',show,name='show'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('total/',total,name='total'),
    path('morning/',morning,name='morning'),
    path('afternoon/',afternoon,name='afternoon'),
    path('evening/',evening,name='evening'),
    path('software/',software,name='software'),
    path('accounts/',accounts,name='accounts'),
    path('multimedia/',multimedia,name='multimedia'),
    path('hardware/',hardware,name='hardware'),
    path('kevin/',kevin,name='kevin'),
    path('kannan/',kannan,name='kannan'),
    path('sairam/',sairam,name='sairam'),
    path('bala/',bala,name='bala'),
    path('search/',search,name="search"),
  
]
