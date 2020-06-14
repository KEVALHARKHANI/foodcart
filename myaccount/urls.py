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
from . import views
from django.urls import path

urlpatterns = [
    path('',views.myaccount,name='myaccount'),
    path('address',views.view_address,name='address'),
    path('address/edit_address/<int:id>',views.edit_address,name='edit'),
    path('edit_add_address',views.edit_add_address,name='add_address'),
    path('delete_address/<int:id>',views.delete_address,name='delete_address'),
    path('new_address',views.new_address,name='new_address'),
    path('add_address',views.new_add_address,name='add_address'),
    path('profile',views.profile,name='profile'),
    path('address/edit_address',views.view_address,name='view_address'),
    path('saved_card',views.saved_card,name="saved_card"),
    path('delete_card/<int:id>',views.card_delete,name="delete_card"),
    path('new_card',views.new_card,name='new_card'),
    path('add_new_card',views.add_to_card,name='add_new_card'),
    path('order_details',views.order_details,name='order_details'),



]
