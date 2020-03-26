import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .serializers import RestaurantSerializer
# Create your tests here.

client = Client()


class GetAllRestaurantsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        kfc_menu = MenuList.objects.create(name='KFC_MENU')
        chicken = Menu.objects.create(
            name='chicken', price='500', units=1, menu_list=kfc_menu)
        rice = Menu.objects.create(
            name='rice', price='200', units=1, menu_list=kfc_menu)
        Restaurant.objects.create(
            name='KFC', address="Lekki", menu_list=kfc_menu)

    def test_get_all_restaurants(self):
        # get API response
        response = client.get(reverse('get_post_restaurant'))
        # get data from db
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class GetSingleRestaurantTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        self.kfc_menu = MenuList.objects.create(name='KFC_MENU')
        self.chicken = Menu.objects.create(
            name='chicken', price='500', units=1, menu_list=self.kfc_menu)
        self.rice = Menu.objects.create(
            name='rice', price='200', units=1, menu_list=self.kfc_menu)
        self.rambo = Restaurant.objects.create(
            name='KFC', address="Lekki", menu_list=self.kfc_menu)

    def test_get_valid_single_restaurant(self):
        response = client.get(
            reverse('get_delete_update_restaurant', kwargs={'pk': self.rambo.pk}))
        restaurant = Restaurant.objects.get(pk=self.rambo.pk)
        serializer = RestaurantSerializer(restaurant)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_restaurant(self):
        response = client.get(
            reverse('get_delete_update_restaurant', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRestaurantTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.kobis = MenuList.objects.create(name='KOBIS_MENU')
        self.valid_payload = {
            'name': 'Kobis',
            'address': 'Admiralty Lekki phase 1',
            'menu_list': 1,
        }
        self.invalid_payload = {
            'name': 'Kobis',
            'address': 'Admiralty, Lekki phase 1',
            'menu_list': 2,
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_restaurant'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_restaurant'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
