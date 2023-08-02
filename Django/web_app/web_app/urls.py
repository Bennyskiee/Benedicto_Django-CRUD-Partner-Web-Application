"""
URL configuration for web_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from car_rent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.customer_index, name='root'), 
    path('client/', views.customer_index, name='customer_index'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/store/', views.customer_store, name='customer_store'),
    path('customers/<int:id>/edit/', views.customer_edit, name='customer_edit'),
    path('customers/<int:id>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:id>/delete/', views.customer_delete, name='customer_delete'),

    path('payments/', views.payment_index, name='payment_index'),
    path('payments/create/', views.payment_create, name='payment_create'),
    path('payments/store/', views.payment_store, name='payment_store'),
    path('payments/<int:id>/edit/', views.payment_edit, name='payment_edit'),
    path('payments/<int:id>/update/', views.payment_update, name='payment_update'),
    path('payments/<int:id>/delete/', views.payment_delete, name='payment_delete'),

    path('rents/', views.rent_index, name='rent_index'),
    path('rents/create/', views.rent_create, name='rent_create'),
    path('rents/store/', views.rent_store, name='rent_store'),
    path('rents/<int:id>/edit/', views.rent_edit, name='rent_edit'),
    path('rents/<int:id>/update/', views.rent_update, name='rent_update'),
    path('rents/<int:id>/delete/', views.rent_delete, name='rent_delete'),

    path('requirements/', views.requirement_index, name='req_index'),
    path('requirements/create/', views.requirement_create, name='req_create'),
    path('requirements/store/', views.requirement_store, name='req_store'),
    path('requirements/<int:id>/edit/', views.requirement_edit, name='req_edit'),
    path('requirements/<int:id>/update/', views.requirement_update, name='req_update'),
    path('requirements/<int:id>/delete/', views.requirement_delete, name='req_delete'),

    path('vehicles/', views.vehicle_index, name='vehicle_index'),
    path('vehicles/create/', views.vehicle_create, name='vehicle_create'),
    path('vehicles/store/', views.vehicle_store, name='vehicle_store'),
    path('vehicles/<int:id>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('vehicles/<int:id>/update/', views.vehicle_update, name='vehicle_update'),
    path('vehicles/<int:id>/delete/', views.vehicle_delete, name='vehicle_delete'),
]
