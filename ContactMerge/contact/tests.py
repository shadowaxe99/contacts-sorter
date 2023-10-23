import unittest
from django.test import TestCase
from contact.models import Contact
from contact.views import merge_contacts

class ContactMergeTestCase(TestCase):
    def setUp(self):
        self.contact1 = Contact.objects.create(name="John Doe", email="john@example.com")
        self.contact2 = Contact.objects.create(name="Jane Smith", email="jane@example.com")
        self.contact3 = Contact.objects.create(name="John Doe", email="john.doe@example.com")

    def test_merge_contacts(self):
        merge_contacts(self.contact1, self.contact3)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertEqual(Contact.objects.filter(name="John Doe").count(), 1)
        self.assertEqual(Contact.objects.filter(email="john.doe@example.com").count(), 1)

        merge_contacts(self.contact2, self.contact3)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.filter(name="Jane Smith").count(), 1)
        self.assertEqual(Contact.objects.filter(email="jane@example.com").count(), 1)

if __name__ == '__main__':
    unittest.main()