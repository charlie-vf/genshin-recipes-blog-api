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
        response = self.client.post('/recipes/', {'title': 'a recipe'})
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_recipe(self):
        response = self.client.post('/recipes/', {'title': 'a recipe'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipeDetailViewTests(APITestCase):
    def setUp(self):
        p = User.objects.create_user(username='p', password='pass')
        c = User.objects.create_user(username='c', password='pass')
        Recipe.objects.create(
            owner=p, title='a recipe', content='stuff'
        )
        Recipe.objects.create(
            owner=c, title='another recipe', content='stuffs'
        )

    def test_can_get_recipe_with_valid_id(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.data['title'], 'a recipe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_recipe_using_invalid_id(self):
        response = self.client.get('/recipes/234/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='p', password='pass')
        response = self.client.put('/recipes/1/', {'title': 'a new recipe'})
        recipe = Recipe.objects.filter(pk=1).first()
        self.assertEqual(recipe.title, 'a new recipe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_recipe(self):
        self.client.login(username='p', password='pass')
        response = self.client.put('/recipes/2/', {'title': 'new recipe'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
