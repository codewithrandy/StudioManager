from django.contrib import admin
from App.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'target', 'gender']
    search_fields = ['name', 'email', 'target']
    list_filter = ['gender']
    list_per_page = 8

admin.site.register(Customer, CustomerAdmin)