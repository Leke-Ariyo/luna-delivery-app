from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single restaurant
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    # delete a single restaurant
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single restaurant
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_restaurant(request):
    # get all restaurants
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    # insert a new record for a restaurant
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'address': request.data.get('address'),
            'menu_list': int(request.data.get('menu_list')),
        }
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
