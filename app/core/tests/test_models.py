from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        ''' Test the creation of user with email '''
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        ''' Tests user's email to be sure
            that the second part of email address is lowercase '''
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='123test'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ''' Test the validation of user's email '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        ''' Test creating superuser '''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
