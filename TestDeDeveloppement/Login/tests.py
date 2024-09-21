from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class UserTests(TestCase):
    def test_signup(self):
        User = get_user_model()
        nbr_of_user_before = User.objects.count()
        user = User.objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='password123'
        )
        nbr_of_user_after = User.objects.count()
        self.assertTrue(nbr_of_user_after == nbr_of_user_before + 1)

    def test_login(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='loginuser',
            email='loginuser@gmail.com',
            password='loginpassword'
        )
        response = self.client.post(reverse('login'), {
            'username': 'loginuser',
            'password': 'loginpassword'
        })

        self.assertEqual(response.status_code, 302)  # Redirection après la connexion
        self.assertRedirects(response, '/dashboard/')  # Vérifie si on est redirigé vers le dashboard