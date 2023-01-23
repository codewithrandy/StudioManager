from django.shortcuts import render
from App.models import Customer
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages


# FUNCTION TO RENDER HOME PAGE
def home(request):
    customer_list = Customer.objects.all()
    return render(request, 'home.html', {'customers':customer_list})


# JSON
def customer_json(request):
    customers = Customer.objects.all()
    data = [customer.get_data() for customer in customers]
    response = {'data': data}
    return JsonResponse(response)


# PATH TO ADD CUSTOMER
def add_customer(request):
    if request.method=='POST':
        if request.POST.get('name') \
            and request.POST.get('email') \
            and request.POST.get('target') \
            and request.POST.get('revenue') \
            and request.POST.get('gender') \
            or request.POST.get('note'):
            customer = Customer()
            customer.name = request.POST.get('name')
            customer.email = request.POST.get('email')
            customer.target = request.POST.get('target')
            customer.revenue = request.POST.get('revenue')
            customer.gender = request.POST.get('gender')
            customer.note = request.POST.get('note')
            customer.save()
            messages.success(request, 'Customer added successfully')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'add.html')


# PATH TO VIEW CUSTOMER
def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if customer != None:
        return render(request, 'edit.html', {'customer': customer})


# PATH TO EDIT CUSTOMER
def edit_customer(request):
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.POST.get('id'))
        if customer != None:
            customer.name = request.POST.get('name')
            customer.email = request.POST.get('email')
            customer.target = request.POST.get('target')
            customer.revenue = request.POST.get('revenue')
            customer.gender = request.POST.get('gender')
            customer.note = request.POST.get('note')
            customer.save()
            messages.success(request, 'Customer updated successfully')
            return HttpResponseRedirect('/')


# PATH TO DELETE CUSTOMER
def delete_customer(request, customer_id):
    customer = Customer.objects.get(id = customer_id)
    customer.delete()
    messages.success(request, 'Customer deleted successfully')
    return HttpResponseRedirect('/')