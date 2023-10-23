import unittest
from utils.deduplicate import remove_duplicates

class TestDeduplicate(unittest.TestCase):
    def test_remove_duplicates(self):
        data = [
            {'name': 'John', 'email': 'john@example.com'},
            {'name': 'Jane', 'email': 'jane@example.com'},
            {'name': 'John', 'email': 'john@example.com'},
            {'name': 'Jane', 'email': 'jane@example.com'},
            {'name': 'John', 'email': 'john@example.com'},
        ]
        expected_result = [
            {'name': 'John', 'email': 'john@example.com'},
            {'name': 'Jane', 'email': 'jane@example.com'},
        ]
        result = remove_duplicates(data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()