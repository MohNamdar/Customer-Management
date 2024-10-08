from django.shortcuts import render, redirect
from .forms import NewOrder, TakePhone
from .models import Order, OrderItem
from club.models import Customer
from django.contrib import messages


# Create your views here.
def new_order(request):
    if request.method == "POST":
        form = TakePhone(request.POST)
        if form.is_valid():
            return redirect('order:add_order', phone=form.cleaned_data['phone'])
    context = {
        'form': TakePhone(),
    }
    return render(request, 'order/new_order.html', context)


def add_order(request, phone):
    customer, created = Customer.objects.get_or_create(phone=phone)
    if request.method == "POST":
        form = NewOrder(request.POST)
        if form.is_valid():
            customer.first_name = form.cleaned_data['first_name']
            customer.last_name = form.cleaned_data['last_name']
            customer.save()

            selected_products = form.cleaned_data['selected_products']
            order = form.save(commit=False)
            order.buyer = customer
            order.save()

            for item in selected_products:
                OrderItem.objects.create(
                    order=order,
                    product=item[0],
                    price=item[0].final_price,
                    quantity=item[1]
                )

            return redirect('order:orders_list')
    form = NewOrder(initial={'first_name': customer.first_name, 'last_name': customer.last_name, 'buyer_phone': phone})
    if created:
        messages.success(request, 'یک مشتری جدید با این شماره همراه ایجاد شد')
    else:
        messages.info(request, 'این مشتری از قبل وجود دارد')
    context = {
        'form': form,
    }
    return render(request, 'order/new_order.html', context)


def orders_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'order/orders_list.html', context)
