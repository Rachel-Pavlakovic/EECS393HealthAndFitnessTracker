"""
WSGI config for HealthAndFitnessTracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from django.test import TestCase


class TestAdmin(TestCase):

    def setUp(self):
        self.client = Client()
        self.my_admin = User(username='user', is_staff=True)
        my_admin.set_password('passphrase') # can't set above because of hashing
        my_admin.save() # needed to save to temporary test db
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        self.assertTrue(loginresponse) # should now return "true"