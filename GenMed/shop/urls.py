from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('updatestock/',views.update_stock, name='update_stock'),
    path('profile/',views.profile, name='profile'),
    path('curstock/',views.cur_stock, name='cur_stock'),
    path('updateinfo/',views.update_info, name='update_info'),
    path('updatecord', views.update_cord, name='update_cord'),
    path('updatelicense', views.update_license, name='update_license'),
    path('shopheader/',views.shopheader, name='shop_header'),
]