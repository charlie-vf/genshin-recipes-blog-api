from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class RecipeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='f', password='pass')

    def test_can_list_recipes(self):
        f = User.objects.get(username='f')
        Recipe.objects.create(owner=f, title='a recipe')

        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_recipes(self):
        self.client.login(username='f', password='pass')
        response = self.client.post('/recipes/', {'title': 'a title'})
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_recipe(self):
        response = self.client.post('/recipes/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
