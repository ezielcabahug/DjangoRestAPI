from rest_framework.test import APITestCase
from rest_framework import status
from api.constants import *

test_list_data = [
    {'brand': 'Suzuki', 'model': 2010},
    {'brand': 'Suzuki', 'model': 2016},
    {'brand': 'Chevrolet', 'model': 2016},
]


class FindTestCase(APITestCase):
    def test_query_both_brand_and_model(self):
        for item in test_list_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        find_brand_model_index = 2
        query_str = "?brand={}&model={}".format(
            test_list_data[find_brand_model_index]['brand'],
            test_list_data[find_brand_model_index]['model']
        )
        find_brand_model_res = self.client.get('/' + URL_FIND + query_str)
        self.assertEqual(len(find_brand_model_res.data), 1)
        self.assertEqual(
            find_brand_model_res.data[0]['brand'],
            test_list_data[find_brand_model_index]['brand']
        )
        self.assertEqual(
            find_brand_model_res.data[0]['model'],
            test_list_data[find_brand_model_index]['model']
        )

    def test_query_brand(self):
        for item in test_list_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        find_brand = 'Suzuki'
        query_str = "?brand={}".format(find_brand)
        find_brand_res = self.client.get('/' + URL_FIND + query_str)
        self.assertEqual(len(find_brand_res.data), 2)
        self.assertEqual(
            find_brand_res.data[0]['brand'],
            test_list_data[0]['brand']
        )
        self.assertEqual(
            find_brand_res.data[0]['model'],
            test_list_data[0]['model']
        )

        self.assertEqual(
            find_brand_res.data[1]['brand'],
            test_list_data[1]['brand']
        )
        self.assertEqual(
            find_brand_res.data[1]['model'],
            test_list_data[1]['model']
        )

    def test_query_model(self):
        for item in test_list_data:
            res = self.client.post('/' + URL_CREATE, item)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        test_model = 2016
        query_str = "?model={}".format(test_model)
        res = self.client.get('/' + URL_FIND + query_str)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(
            res.data[0]['brand'],
            test_list_data[1]['brand']
        )
        self.assertEqual(
            res.data[0]['model'],
            test_list_data[1]['model']
        )

        self.assertEqual(
            res.data[1]['brand'],
            test_list_data[2]['brand']
        )
        self.assertEqual(
            res.data[1]['model'],
            test_list_data[2]['model']
        )
