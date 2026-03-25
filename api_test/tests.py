from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AuthTests(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpass123"
        self.user = User.objects.create_superuser(
            username=self.username,
            password=self.password
        )
        self.token_url = reverse('token_obtain_pair')
        self.swagger_url = reverse('swagger-ui')

    def test_get_token_success(self):
        data = {"username": self.username, "password": self.password}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_swagger_ui_access(self):
        response = self.client.get(self.swagger_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token_fail(self):
        data = {"username": self.username, "password": "yanlis_sifre_123"}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_token_missing_fields(self):
        data = {"username": self.username}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_get_token_invalid_user(self):
        data = {"username": "hayali_kullanici", "password": "sifre123"}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ContentTests(APITestCase):
    fixtures = ['contents.json']

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser", password="testpass123"
        )
        token_response = self.client.post(
            reverse('token_obtain_pair'),
            {"username": "testuser", "password": "testpass123"},
            format='json'
        )
        self.token = token_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.content_url = reverse('content-list')

    def test_content_list_authenticated(self):
        response = self.client.get(self.content_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)

    def test_content_list_unauthenticated(self):
        self.client.credentials()
        response = self.client.get(self.content_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_by_title(self):
        response = self.client.get(self.content_url, {'title': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertIn('django', item['title'].lower())

    def test_filter_by_desc(self):
        response = self.client.get(self.content_url, {'desc': 'guide'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertIn('guide', item['desc'].lower()) 