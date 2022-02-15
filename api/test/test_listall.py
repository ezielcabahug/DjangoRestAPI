from rest_framework.test import APITestCase
from rest_framework import status
from api.constants import *

test_data = [
    {'brand': 'Suzuki', 'model': 2010},
    {'brand': 'Suzuki', 'model': 2016},
    {'brand': 'Chevrolet', 'model': 2016},
]


class ListAllTestCase(APITestCase):
    def test_listall_should_list_all_data(self):
        for item in test_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.get('/' + URL_LIST_ALL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(test_data))

        first_data = res.data[0]
        last_data = res.data[2]
        self.assertEqual(first_data['brand'], test_data[0]['brand'])
        self.assertEqual(last_data['model'], test_data[2]['model'])
