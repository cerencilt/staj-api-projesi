from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def setUp(self):
        # Test kullanıcısı oluştur
        self.username = "testuser"
        self.password = "testpass123"
        self.user = User.objects.create_superuser(
            username=self.username, 
            password=self.password
        )
        # Url'lerin 'urls.py' dosyasındaki 'name' kısımlarıyla eşleştiğinden emin ol
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