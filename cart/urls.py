"""foodcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cart import views
from django.urls import path

urlpatterns = [
    path('',views.cart1,name='cart'),
    path('add',views.add_to_cart,name='add'),
    path('delete',views.fdelete,name='delete'),
    path('cadd',views.fadd,name='cart_add_food'),
    path('remove',views.remove,name='food_remove'),
    path('new_address',views.new_address,name='naddress'),
    path('zipcode',views.zipcode,name='zipcode'),
    path('add_address',views.add_address,name='add_address'),
    path('procced',views.check_address,name='procced'),
    path('select_address',views.select_address,name='select_address'),
    path('checkout',views.checkout,name='checkout'),
    path('payment',views.payment,name='payment'),
    path('add_to_card',views.add_to_card,name="add_to_card"),
    path('payment_method',views.payment_method,name='payment_method'),


]
