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

def test_refresh_token_success(self):
    login_data = {"username": self.username, "password": self.password}
    login_response = self.client.post(self.token_url, login_data, format='json')
    refresh_token = login_response.data['refresh']
    refresh_url = reverse('token_refresh') 
    response = self.client.post(refresh_url, {"refresh": refresh_token}, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('access', response.data)