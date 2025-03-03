from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Kunde

class KundeAPITests(APITestCase):

    def setUp(self):
        self.kunde = Kunde.objects.create(vorname="Test", nachname="User")

    def test_get_kunden_liste(self):
        response = self.client.get('/api/kunden/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_kunde(self):
        data = {"vorname": "Max", "nachname": "Müller", "mail": "max@example.com"}
        response = self.client.post('/api/kunden/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Kunde.objects.count(), 2)
