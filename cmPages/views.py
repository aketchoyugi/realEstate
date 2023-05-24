from django.shortcuts import render
from django.http import HttpResponse
from houses.options import price_choices, bedroom_choices, county_choices

from houses.models import House
from salesPersons.models import SalesPerson

# Create your views here.

def index(request):
    houses = House.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'houses': houses,
        'county_choices': county_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'cmPages/home.html', context)


def about(request):
    salesPersons = SalesPerson.objects.order_by('-hire_date')

    mvp_salesperson = SalesPerson.objects.all().filter(is_mvp=True)

    context = {
        'salesPerson':salesPersons,
        'mvp_salesPerson':mvp_salesperson
    }

    return render (request, 'cmPages/about.html', context)

