from django.shortcuts import render, redirect
from .models import Customer, Payment, Rent, Requirements, Vehicle

def customer_index(request):
    results = 15
    number_of_results = Customer.objects.count()
    number_of_pages = (number_of_results / results)

    page = request.GET.get('page', 1)
    page_first = (page - 1) * results

    customers = Customer.objects.order_by('lastname') \
                               .all()[page_first:page_first+results]

    return render(request, 'client.html', {
        'customers': customers,
        'number_of_pages': number_of_pages
    })

def customer_create(request):
    return render(request, 'client_create.html')

def customer_store(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        contact = request.POST.get('contact')

        Customer.objects.create(
            firstname=firstname,
            lastname=lastname,
            address=address,
            contact=contact
        )

        return redirect('customer_index')

def customer_edit(request, id):
    customer = Customer.objects.filter(customer_id=id).first()

    if customer:
        return render(request, 'client_edit.html', {'customer': customer})

    return redirect('customer_index')

def customer_update(request, id):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        contact = request.POST.get('contact')

        customer = Customer.objects.filter(customer_id=id).first()

        if customer:
            customer.firstname = firstname
            customer.lastname = lastname
            customer.address = address
            customer.contact = contact
            customer.save()

        return redirect('customer_index')

def customer_delete(request, id):
    customer = Customer.objects.filter(customer_id=id).first()

    if customer:
        customer.delete()

    return redirect('customer_index')

def payment_index(request):
    results = 15
    number_of_results = Payment.objects.count()
    number_of_pages = (number_of_results / results)

    page = request.GET.get('page', 1)
    page_first = (page - 1) * results

    payments = Payment.objects.order_by('payment_id') \
                              .all()[page_first:page_first+results]

    return render(request, 'payments.html', {
        'payments': payments,
        'number_of_pages': number_of_pages
    })

def payment_create(request):
    return render(request, 'payments_create.html')

def payment_store(request):
    if request.method == 'POST':
        rent_id = request.POST.get('rent_id')
        mode_payment = request.POST.get('mode_payment')
        balance = request.POST.get('balance')

        Payment.objects.create(
            rent_id=rent_id,
            mode_payment=mode_payment,
            balance=balance
        )

        return redirect('payment_index')

def payment_edit(request, id):
    payment = Payment.objects.filter(payment_id=id).first()

    if payment:
        return render(request, 'payments_edit.html', {'payment': payment})

    return redirect('payment_index')

def payment_update(request, id):
    if request.method == 'POST':
        rent_id = request.POST.get('rent_id')
        mode_payment = request.POST.get('mode_payment')
        balance = request.POST.get('balance')

        payment = Payment.objects.filter(payment_id=id).first()

        if payment:
            payment.rent_id = rent_id
            payment.mode_payment = mode_payment
            payment.balance = balance
            payment.save()

        return redirect('payment_index')

def payment_delete(request, id):
    payment = Payment.objects.filter(payment_id=id).first()

    if payment:
        payment.delete()

    return redirect('payment_index')

def rent_index(request):
    results = 10
    number_of_results = Rent.objects.count()
    number_of_pages = (number_of_results / results)

    page = request.GET.get('page', 1)
    page_first = (page - 1) * results

    rents = Rent.objects.order_by('rent_id') \
                        .all()[page_first:page_first+results]

    return render(request, 'rents.html', {
        'rents': rents,
        'number_of_pages': number_of_pages
    })

def rent_create(request):
    return render(request, 'rents_create.html')

def rent_store(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        vehicle_id = request.POST.get('vehicle_id')
        rent_start = request.POST.get('rent_start')
        rent_end = request.POST.get('rent_end')

        Rent.objects.create(
            customer_id=customer_id,
            vehicle_id=vehicle_id,
            rent_start=rent_start,
            rent_end=rent_end
        )

        return redirect('rent_index')

def rent_edit(request, id):
    rent = Rent.objects.filter(rent_id=id).first()

    if rent:
        return render(request, 'rents_edit.html', {'rent': rent})

    return redirect('rent_index')

def rent_update(request, id):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        vehicle_id = request.POST.get('vehicle_id')
        rent_start = request.POST.get('rent_start')
        rent_end = request.POST.get('rent_end')

        rent = Rent.objects.filter(rent_id=id).first()

        if rent:
            rent.customer_id = customer_id
            rent.vehicle_id = vehicle_id
            rent.rent_start = rent_start
            rent.rent_end = rent_end
            rent.save()

        return redirect('rent_index')

def rent_delete(request, id):
    rent = Rent.objects.filter(rent_id=id).first()

    if rent:
        rent.delete()

    return redirect('rent_index')


def requirement_index(request):
    results = 10
    number_of_results = Requirements.objects.count()
    number_of_pages = (number_of_results / results)

    page = request.GET.get('page', 1)
    page_first = (page - 1) * results

    requirements = Requirements.objects.order_by('requirements_id') \
                                      .all()[page_first:page_first+results]

    return render(request, 'req.html', {
        'requirements': requirements,
        'number_of_pages': number_of_pages
    })

def requirement_create(request):
    return render(request, 'req_create.html')

def requirement_store(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        requirement = request.POST.get('requirement')

        Requirements.objects.create(
            customer_id=customer_id,
            requirement=requirement
        )

        return redirect('req_index')

def requirement_edit(request, id):
    requirements = Requirements.objects.filter(requirements_id=id).first()

    if requirements:
        return render(request, 'req_edit.html', {'requirements': requirements})

    return redirect('req_index')

def requirement_update(request, id):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        requirement = request.POST.get('requirement')

        requirements = Requirements.objects.filter(requirements_id=id).first()

        if requirements:
            requirements.customer_id = customer_id
            requirements.requirement = requirement
            requirements.save()

        return redirect('req_index')

def requirement_delete(request, id):
    requirements = Requirements.objects.filter(requirements_id=id).first()

    if requirements:
        requirements.delete()

    return redirect('req_index')


def vehicle_index(request):
    results = 10
    number_of_results = Vehicle.objects.count()
    number_of_pages = (number_of_results / results)

    page = request.GET.get('page', 1)
    page_first = (page - 1) * results

    vehicles = Vehicle.objects.order_by('vehicle_id') \
                              .all()[page_first:page_first+results]

    return render(request, 'vehicle.html', {
        'vehicles': vehicles,
        'number_of_pages': number_of_pages
    })

def vehicle_create(request):
    return render(request, 'vehicle_create.html')

def vehicle_store(request):
    if request.method == 'POST':
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_type = request.POST.get('vehicle_type')
        color = request.POST.get('color')
        plate = request.POST.get('plate')
        vehicle_status = request.POST.get('vehicle_status')

        Vehicle.objects.create(
            vehicle_model =vehicle_model,
            vehicle_type=vehicle_type,
            plate=plate,
            color=color,
            vehicle_status=vehicle_status
        )

        return redirect('vehicle_index')

def vehicle_edit(request, id):
    vehicle = Vehicle.objects.filter(vehicle_id=id).first()

    if vehicle:
        return render(request, 'vehicle_edit.html', {'vehicle': vehicle})

    return redirect('vehicle_index')

def vehicle_update(request, id):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_type = request.POST.get('vehicle_type')
        color = request.POST.get('color')
        plate = request.POST.get('plate')
        vehicle_status = request.POST.get('vehicle_status')

        vehicle = Vehicle.objects.filter(vehicle_id=id).first()

        vehicle.vehicle_id = vehicle_id
        vehicle.vehicle_model = vehicle_model
        vehicle.vehicle_type = vehicle_type
        vehicle.color = color
        vehicle.plate = plate
        vehicle.vehicle_status = vehicle_status
        vehicle.save()

        return redirect('vehicle_index')

def vehicle_delete(request, id):
    vehicle = Vehicle.objects.filter(vehicle_id=id).first()

    if vehicle:
        vehicle.delete()

    return redirect('vehicle_index')
