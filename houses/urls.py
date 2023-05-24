from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='houses'),
    path('<int:house_id>', views.house, name='house'),
    path('search', views.search, name='search'),
]
