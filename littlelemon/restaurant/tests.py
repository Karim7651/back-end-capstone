from django.test import TestCase
from .models import MenuItem, Booking

# Create your tests here.

class MenuTest(TestCase):
    
    def test_get_item(self):
        menu_item = MenuItem.objects.create(title="Hotsilog", price=25,inventory=100)
        
        self.assertEqual(str(menu_item), 'Hotsilog : 25')


class BookingTest(TestCase):

    def test_get_booking_item(self):

        booking_item = Booking.objects.create(name="karim", no_of_guests=2, booking_date='2023-09-09')

        self.assertEqual(str(booking_item), 'karim')