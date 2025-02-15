import unittest

from billomapy.billomapy import Billomapy


class TestBillomapy(unittest.TestCase):
    def test_init(self):
        billomapy = Billomapy('TEST_ID', 'API_KEY', 'APP_ID', 'APP_SECRET')
        self.assertEqual(billomapy.billomat_id, 'TEST_ID')
        self.assertEqual(billomapy.api_key, 'API_KEY')
        self.assertEqual(billomapy.app_id, 'APP_ID')
        self.assertEqual(billomapy.app_secret, 'APP_SECRET')
        self.assertEqual(billomapy.api_url, 'https://TEST_ID.billomat.net/api/')


if __name__ == '__main__':
    unittest.main()
