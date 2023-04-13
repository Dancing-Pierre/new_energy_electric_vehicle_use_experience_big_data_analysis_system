"""new_energy_car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_car.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('do_login', do_login),
    path('car_list', car_list),
    path('get_car_list', get_car_list),
    path('car_price', car_price),
    path('car_price_data', car_price_data),
    path('energy_range_min_price', energy_range_min_price),
    path('energy_range_max_price', energy_range_max_price),
    path('energy_range_min_price_data', energy_range_min_price_data),
    path('energy_range_max_price_data', energy_range_max_price_data),
    path('car_subsidy', car_subsidy),
    path('car_price_bar', car_price_bar),
    path('car_price_bar_data', car_price_bar_data),
    path('car_pure_energy_bar', car_pure_energy_bar),
    path('car_pure_energy_bar_data', car_pure_energy_bar_data),
]
