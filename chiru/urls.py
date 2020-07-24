from django.urls import path
from chiru import views

app_name="chiru" #is used to create a namespace

urlpatterns = [
    path('',views.index,name="index"),
    #path of (secondary suffix,address of function,nameof mapping)
    path('home',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
]
