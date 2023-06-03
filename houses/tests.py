from django.test import TestCase, RequestFactory
from salesPersons.models import SalesPerson
from datetime import datetime
from django.utils import timezone
from .models import House
from .views import index, search, house
from django.urls import reverse

class HouseModelTest(TestCase):

    def setUp(self):
        hire_date = timezone.now()  # Get the current time in the default timezone
        self.sales_person = SalesPerson.objects.create(name='John Doe', hire_date=hire_date)
        list_date = timezone.now()  # Get the current time in the default timezone
        self.house = House.objects.create(
            SalesPerson=self.sales_person,
            title='Test House',
            address='123 Test St',
            town='Test Town',
            county='Test County',
            postcode='12345',
            description='This is a test house',
            price=100000,
            bedrooms=3,
            bathrooms=2.5,
            garage=1,
            sqft=1500,
            lot_size=0.25,
            is_published=True,
            list_date=list_date
        )
    

    def test_house_creation(self):

        list_date = timezone.now()
        house = House.objects.create(
           
            list_date=list_date
        )

        self.assertEqual(self.house.title, 'Test House')
        self.assertEqual(self.house.address, '123 Test St')
        # Add more assertions for other fields as needed



class HouseViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.house = House.objects.create(title='Test House', 
        description='This is a test house',
        price=12222,
        bedrooms=3,
        bathrooms=2.5,
        garage=1,
        sqft=1500,
        lot_size=0.25,
        is_published=True,
        list_date=timezone.now()
        )

    def test_index_view(self):
        request = self.factory.get(reverse('houses:index'))
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'houses/houses.html')
        # Add more assertions as needed

    def test_house_view(self):
        request = self.factory.get(reverse('houses:house', args=(self.house.id,)))
        response = house(request, house_id=self.house.id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'houses/house.html')
        # Add more assertions as needed

    def test_search_view(self):
        request = self.factory.get(reverse('houses:search'), {'keywords': 'test'})
        response = search(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'houses/search.html')
        # Add more assertions as needed