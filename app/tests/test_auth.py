from cgitb import reset
import unittest

from app.src import db
from app.src.models.blacklist import BlacklistToken
import json
from app.tests.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='joe@gmail.com',
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='joe@gmail.com',
            password='123456'
        )),
        content_type='application/json'
    )


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        """ Test for user registration """
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""
        register_user(self)
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(
                data['message'] == 'User with that email already exists')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.'
            )
            self.assertTrue(data_register['Authorization'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_non_registered_user_login(self):
        """ Test for login of non-registered user """
        with self.client:
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            print(data['message'])
            self.assertTrue(data['message'] == 'email or password does not match.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()