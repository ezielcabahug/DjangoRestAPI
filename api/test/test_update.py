from rest_framework.test import APITestCase
from rest_framework import status
from api.constants import *

test_data = [
    {'brand': 'Suzuki', 'model': 2010},
    {'brand': 'Suzuki', 'model': 2016},
    {'brand': 'Chevrolet', 'model': 2016},
]


class UpdateTestCase(APITestCase):
    def test_edit_the_data(self):
        for item in test_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.get('/' + URL_LIST_ALL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        first_data = res.data[0]
        self.assertEqual(first_data['brand'], test_data[0]['brand'])
        self.assertEqual(first_data['model'], test_data[0]['model'])

        first_change = {'brand': 'Opel', 'model': 2010}
        res = self.client.put('/' + URL_UPDATE + '/1', first_change)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res = self.client.get('/' + URL_LIST_ALL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        first_data = res.data[0]
        self.assertEqual(first_data['brand'], first_change['brand'])
        self.assertEqual(first_data['model'], first_change['model'])
