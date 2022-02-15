from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.constants import *

valid_data = [
    {'brand': 'Suzuki', 'model': 2010},
    {'brand': 'Suzuki', 'model': 2016},
    {'brand': 'Chevrolet', 'model': 2016},
]

invalid_data = [
    {'brands': 'Suzuki', 'model': 2010},
    {'brand': 'Suzuki', 'models': 2016},
    {'brand': 'Chevrolet', 'model': 'twenty sixteen'}
]


class CreateTestCase(APITestCase):
    def test_create_valid_data(self):
        for items in valid_data:
            res = self.client.post('/' + URL_CREATE, items)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_data(self):
        for item in invalid_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        res = self.client.post('/' + URL_CREATE, {})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        res = self.client.post('/' + URL_CREATE)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
