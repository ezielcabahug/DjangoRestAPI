# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cars
from .serializers import CarsSerializer


@api_view(['GET'])
def list_all(req):
    cars_list = Cars.objects.all()
    serializer = CarsSerializer(cars_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(req):
    serializer = CarsSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(req, car_id):
    car = Cars.objects.get(pk=car_id)
    serializer = CarsSerializer(car, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find(req):
    if 'brand' in req.query_params and 'model' in req.query_params:
        cars_list = Cars.objects.filter(
            brand=req.query_params['brand'],
            model=req.query_params['model']
        )
        serializer = CarsSerializer(cars_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif 'brand' in req.query_params:
        cars_list = Cars.objects.filter(
            brand=req.query_params['brand']
        )
        serializer = CarsSerializer(cars_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif 'model' in req.query_params:
        cars_list = Cars.objects.filter(
            model=req.query_params['model']
        )
        serializer = CarsSerializer(cars_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response([], status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(req, car_id):
    car = Cars.objects.filter(pk=car_id)
    if car.exists():
        return_data = {
            'id': car_id,
            'brand': car[0].brand,
            'model': car[0].model
        }
        car.delete()
        return Response(return_data, status=status.HTTP_202_ACCEPTED)
    return Response({'id': car_id}, status=status.HTTP_400_BAD_REQUEST)
