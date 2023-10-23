import unittest
import pandas as pd
from utils.unification import unify_contacts

class TestUnification(unittest.TestCase):
    def test_unify_contacts(self):
        # Test case 1: Same contact with different spellings
        contacts = pd.DataFrame({
            'Name': ['John Doe', 'John Doe', 'John Doe'],
            'Email': ['john.doe@example.com', 'johndoe@example.com', 'johndoe@example.com'],
            'Phone': ['1234567890', '123-456-7890', '123 456 7890']
        })
        expected_result = pd.DataFrame({
            'Name': ['John Doe'],
            'Email': ['john.doe@example.com'],
            'Phone': ['1234567890']
        })
        self.assertTrue(unify_contacts(contacts).equals(expected_result))

        # Test case 2: Different contacts
        contacts = pd.DataFrame({
            'Name': ['John Doe', 'Jane Smith'],
            'Email': ['john.doe@example.com', 'jane.smith@example.com'],
            'Phone': ['1234567890', '9876543210']
        })
        expected_result = pd.DataFrame({
            'Name': ['John Doe', 'Jane Smith'],
            'Email': ['john.doe@example.com', 'jane.smith@example.com'],
            'Phone': ['1234567890', '9876543210']
        })
        self.assertTrue(unify_contacts(contacts).equals(expected_result))

if __name__ == '__main__':
    unittest.main()