import unittest
from django.test import TestCase
from contact_app.models import Contact

class ContactModelTest(TestCase):
    def setUp(self):
        Contact.objects.create(name='John Doe', email='johndoe@example.com')

    def test_contact_name(self):
        contact = Contact.objects.get(name='John Doe')
        self.assertEqual(contact.name, 'John Doe')

    def test_contact_email(self):
        contact = Contact.objects.get(email='johndoe@example.com')
        self.assertEqual(contact.email, 'johndoe@example.com')

if __name__ == '__main__':
    unittest.main()