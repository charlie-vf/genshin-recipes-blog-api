from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):

    def setUp(self):
        felix = User.objects.create_user(
            username='felix', password='password1')

    def test_list_all_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_profile_with_valid_id(self):
        response = self.client.get('/profiles/1/')


class ProfileDetailViewTests(APITestCase):

    def setUp(self):
        felix = User.objects.create_user(
            username='felix', password='password1')
        charlie = User.objects.create_user(
            username='charlie', password='password2')

    def test_can_update_own_profile(self):
        self.client.login(username='felix', password='password1')
        response = self.client.put('/profiles/1', {'content': 'food'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.content, 'food')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_update_other_user_profile(self):
        self.client.login(username='felix', password='password1')
        response = self.client.put('/profiles/2', {'content': 'food'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
