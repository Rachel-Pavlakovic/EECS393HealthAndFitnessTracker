import unittest
from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
from django.test import Client

class TestAuth(TestCase):

        def setUp(self):
            my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', '12345')
            my_admin.save()

#Need to add non hardcoded values, need to add anonymous check/should block on entering the homepage
        def test_call_view_denies_anonymous(self):
            response = self.client.get('/', follow=True)
            self.assertRedirects(response, '/login/')
            response = self.client.post('/', follow=True)
            self.assertRedirects(response, '/login/')

#Should successfully go into the homepage after login
        def test_call_view_loads(self):
            self.client.login(username='user', password='test')
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'home.html')

#Should be on the same login page on a fail login / not yet implemented in permissions
        def test_call_view_deny_login(self):
            self.client.login(username='myuser', password='')
            user = auth.get_user(self.client)
            assert user.is_authenticated()