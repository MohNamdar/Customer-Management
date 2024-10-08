from django.shortcuts import render
from club.models import Customer


# Create your views here.
def index(request):
    return render(request, 'club/index.html')


def customers_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'club/customers_list.html', context)
