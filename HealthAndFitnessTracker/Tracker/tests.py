import unittest
from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from django.test import Client

from django.contrib import auth
class TestAuth(TestCase):

        def setUp(self):
            my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', '12345')
            my_admin.save()
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            User.objects.create_user(**self.credentials)

#Need to add non hardcoded values, need to add anonymous check/should block on entering the homepage
        def test_call_view_denies_anonymous_foodTracker(self):
            client = Client()
            # it returns AnonymousUser
            response = client.get('/foodTracker', follow=True)
            self.assertRedirects(response, '/login/?next=/foodTracker')
        def test_call_view_denies_anonymous_waterTracker(self):
            client = Client()
            # it returns AnonymousUser
            response = client.get('/waterTracker', follow=True)
            self.assertRedirects(response, '/login/?next=/waterTracker')
        def test_call_view_denies_anonymous_exerciseTracker(self):
            client = Client()
            # it returns AnonymousUser
            response = client.get('/exerciseTracker', follow=True)
            self.assertRedirects(response, '/login/?next=/exerciseTracker')
        def test_call_view_denies_anonymous_settingsAndProfile(self):
            client = Client()
            # it returns AnonymousUser
            response = client.get('/settingsAndProfile', follow=True)
            self.assertRedirects(response, '/login/?next=/settingsAndProfile')

#Should successfully go into the homepage after login
        def test_call_view_loads_home(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertRedirects(response, 'home.html')
        def test_call_view_loads_foodTracker(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/foodTracker')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, ('foodTracker.html')
        def test_call_view_loads_waterTracker(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/waterTracker')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'waterTracker.html')
        def test_call_view_loads_exerciseTracker(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/exerciseTracker')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'exerciseTracker.html')
        def test_call_view_loads_settingsAndProfile(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/settingsAndProfile')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'settingsAndProfile.html')