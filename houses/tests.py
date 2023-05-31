from django.test import TestCase
from salesPersons.models import SalesPerson
from datetime import datetime
from .models import House

class HouseModelTest(TestCase):
    def setUp(self):
        self.sales_person = SalesPerson.objects.create(name='John Doe')
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
            list_date=datetime.now(timezone.utc)
        )

    def test_house_creation(self):
        self.assertEqual(self.house.title, 'Test House')
        self.assertEqual(self.house.address, '123 Test St')
        # Add more assertions for other fields as needed
