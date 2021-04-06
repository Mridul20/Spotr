from django.test import TestCase
from main.forms import CreateUserForm

class TestForms(TestCase):

    def test_valid(self): #Valid Deatails
        form = CreateUserForm(data = {
            'username' : 'gaaa123',
            'first_name' : 'gurjar',
            'email' : 'piyushgurjar@gmail.com',
            'password1' : 'piyush123',
            'password2' : 'piyush123'
        })
        self.assertTrue(form.is_valid())

    def test_username_password_similarity(self): #Password Is to similiar to username
        form = CreateUserForm(data = {
            'username' : 'piyush123',
            'first_name' : 'piyush',
            'email' : 'piyushgurjar@gmail.com',
            'password1' : 'piyush123',
            'password2' : 'piyush123'
        })
        self.assertFalse(form.is_valid())

    def test_password_mismatch(self): #Password Mismatch
        form = CreateUserForm(data = {
            'username' : 'gaaa123',
            'first_name' : 'gurjar',
            'email' : 'piyushgurjar@gmail.com',
            'password1' : 'piyush1233',
            'password2' : 'piyush123'
        })
        self.assertFalse(form.is_valid())

    def test_password_size(self): #Password Too Small
        form = CreateUserForm(data = {
            'username' : 'gaaa123',
            'first_name' : 'gurjar',
            'email' : 'piyushgurjar@gmail.com',
            'password1' : 'p',
            'password2' : 'p'
        })
        self.assertFalse(form.is_valid())

    def test_gmail_invalid(self): #Gmail Invalid
        form = CreateUserForm(data = {
            'username' : 'gaaa123',
            'first_name' : 'gurjar',
            'email' : 'piyushgurjar',
            'password1' : 'piyush123',
            'password2' : 'piyush123'
        })
        self.assertFalse(form.is_valid())

    def test_empty_fields(self): #Empty Fields Check
        form = CreateUserForm(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)