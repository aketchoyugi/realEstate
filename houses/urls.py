from django.urls import path

from . import views

app_name = 'houses'

urlpatterns = [
    path('', views.index, name='houses'),
    path('<int:house_id>', views.house, name='house'),
    path('search', views.search, name='search'),
]
