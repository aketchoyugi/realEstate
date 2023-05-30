from django.contrib import admin
from .models import House

# Register your models here.

class HouseAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'SalesPerson')
  list_display_links = ('id', 'title')
  list_filter = ('SalesPerson',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'county', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(House, HouseAdmin)
