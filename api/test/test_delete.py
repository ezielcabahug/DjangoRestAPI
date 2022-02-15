from rest_framework.test import APITestCase
from rest_framework import status
from api.constants import *

test_data = [
    {'brand': 'Suzuki', 'model': 2011},
    {'brand': 'Suzuki', 'model': 2012},
    {'brand': 'Suzuki', 'model': 2013},
]


class DeleteTestCases(APITestCase):
    def create_data(self):
        for item in test_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def get_number_of_entries(self):
        res = self.client.get('/' + URL_LIST_ALL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return len(res.data)

    def test_delete_data(self):
        self.create_data()
        number_of_entries = self.get_number_of_entries()
        res = self.client.delete('/' + URL_DELETE + '/1')
        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

        new_num_of_entries = self.get_number_of_entries()
        self.assertEqual(number_of_entries - 1, new_num_of_entries)

    def test_delete_invalid_id(self):
        self.create_data()
        number_of_entries = self.get_number_of_entries()
        res = self.client.delete('/' + URL_DELETE + '/4')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        new_num_of_entries = self.get_number_of_entries()
        self.assertEqual(number_of_entries, new_num_of_entries)

    def test_delete_no_id(self):
        self.create_data()
        number_of_entries = self.get_number_of_entries()
        res = self.client.delete('/' + URL_DELETE)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

        new_num_of_entries = self.get_number_of_entries()
        self.assertEqual(number_of_entries, new_num_of_entries)
