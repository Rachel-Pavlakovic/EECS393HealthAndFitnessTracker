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

#Should test an anonymous user attempting to view data
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
            self.assertTemplateUsed(response, 'home.html')
        def test_call_view_loads_foodTracker(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/foodTracker')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'foodTracker.html')
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

#Should test normal users attempting to access admin and admin users trying

        def test_call_view_loads_admin_user(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/admin/')
            self.assertEqual(response.status_code, 302)

        def test_call_view_loads_admin_admin(self):
            self.client.login(username='myuser', password='12345')
            response = self.client.get('/admin/')
            self.assertEqual(response.status_code, 200)


#Should test the logout function TODO

        def test_call_view_logout_foodTrackerTest(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/foodTracker')
            self.assertEqual(response.status_code, 200)
            self.assertRedirects(response, 'foodTracker.html')
            self.client.logout()
            response = self.client.get('/foodTracker')
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/login/?next=/foodTracker')

#Should test adding a new food item to user's listings / new exercise / new drink / etc. TODO

        def test_add_food(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/foodTracker')
            self.assertEqual(response.status_code, 200)
            #client should attempt to get to food client page
            #client should POST its input
            #input saved to client's tuple related
            #input can be retrieved from database

        def test_add_drink(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/waterTracker')
            self.assertEqual(response.status_code, 200)
            # client should attempt to get to water client page
            # client should POST its input
            # input saved to client's tuple related
            # input can be retrieved from database

        #alert/reminder page TODO
        def test_add_alert(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/alertTracker')
            self.assertEqual(response.status_code, 200)
            # client should attempt to get to reminder creation client page
            # client should POST its input
            # input saved to client's tuple related
            # input can be retrieved from database

        #alert/reminder page TODO
        def test_add_alert(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/alertTracker')
            self.assertEqual(response.status_code, 200)
            # client should attempt to get to alert creation client page
            # client should POST its input
            # input saved to client's tuple related
            # input can be retrieved from database

        def test_add_exercise(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/exerciseTracker')
            self.assertEqual(response.status_code, 200)
            #client should attempt to get to exercise client page
            #client should POST its input
            #input saved to client's tuple related
            #input can be retrieved from database


#Should test deleting a food item to user's listings / new exercise / new drink / etc. TODO

        def test_delete_food(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/foodTracker')
            self.assertEqual(response.status_code, 200)
            #client should attempt to get to food client page
            #client should POST its input
            #input saved to client's tuple related
            #input can be deleted from database

        def test_delete_drink(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/waterTracker')
            self.assertEqual(response.status_code, 200)
            # client should attempt to get to water client page
            # client should POST its input
            # input saved to client's tuple related
            #input can be deleted from database

        #alert/reminder page TODO
        def test_delete_alert(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/alertTracker')
            self.assertEqual(response.status_code, 200)
            # client should attempt to get to reminder creation client page
            # client should POST its input
            # input saved to client's tuple related
            #input can be deleted from database

        #alert/reminder page TODO
        def test_delete_alert(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/alertTracker')
            self.assertEqual(response.status_code, 200)
            # client should attempt to get to alert creation client page
            # client should POST its input
            # input saved to client's tuple related
            #input can be deleted from database

        def test_delete_exercise(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/exerciseTracker')
            self.assertEqual(response.status_code, 200)
            #client should attempt to get to exercise client page
            #client should POST its input
            #input saved to client's tuple related
            #input can be deleted from database

#Should test settings TODO
        def test_settings_preview(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/settingsAndProfile')
            self.assertEqual(response.status_code, 200)
            #test if preview is working on new selection

        def test_settings_logininfo(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/settingsAndProfile')
            self.assertEqual(response.status_code, 200)
            #client should POST its input
            #input saved to client's tuple related
            #input can be retrieved from database
            #deletion of old, and adding of new
            user = User.objects.get(username='testuser')
            self.assertEqual(user.check_password('changedpassword'), True)
            #change back
            self.assertEqual(user.check_password('secret'), True)

        def test_settings_userinterface(self):
            self.client.login(username='testuser', password='secret')
            response = self.client.get('/settingsAndProfile')
            self.assertEqual(response.status_code, 200)
            #client should POST its input
            #input saved to client's tuple related
            #old tuple replaced from database