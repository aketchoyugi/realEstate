from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .options import price_choices, bedroom_choices, county_choices

from .models import House

# Create your views here.

def index(request):
  houses = House.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(houses, 6)
  page = request.GET.get('page')
  paged_houses = paginator.get_page(page)

  context = {
    'houses': paged_houses
  }

  return render(request, 'houses/houses.html', context)

def house(request, house_id):
  house = get_object_or_404(House, pk=house_id)

  context = {
    'house' : house
  }

  return render(request, 'houses/house.html', context)

def search(request):
  queryset_list = House.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # County
  if 'county' in request.GET:
    state = request.GET['county']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'county_choices': county_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'houses': queryset_list,
    'values': request.GET
  }

  return render(request, 'houses/search.html', context)



