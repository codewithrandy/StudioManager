from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    # Home Page
    path('', views.home, name='home'),
    # JSON Response
    path('json/', views.customer_json, name='customer_json'),
    # PATH TO ADD CUSTOMER
    path('add_customer', views.add_customer, name='add_customer'),
    # PATH TO VIEW CUSTOMER
    path('customer/<str:customer_id>', views.home, name='customer'),
    # PATH TO EDIT CUSTOMER
    path('edit_customer', views.edit_customer, name='edit_customer'),
    # PATH TO DELETE CUSTOMER
    path('delete_customer/<str:customer_id>', views.delete_customer, name='delete_customer'),
]   
