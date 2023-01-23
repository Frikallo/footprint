import os
import unittest

class TestFootprint(unittest.TestCase):
    def testFootprint(self):
        # Test that running footprint with no arguments returns a 1 exit code, as well as creates a config file
        self.assertEqual(os.system('python -m footprint'), 1)
        self.assertTrue(os.path.exists('./footprint/.conf'))
        # Test that running footprint with an email returns a 200 exit code
        self.assertEqual(os.system('python -m footprint example@example.com'), 200)
        # Test that running footprint set with a valid <api> and a <key> returns a 200 exit code
        self.assertEqual(os.system('python -m footprint set hunter ApiKey'), 200)
        # Test that running footprint set with an invalid <api> and a <key> returns a 0 exit code
        self.assertEqual(os.system('python -m footprint set invalid_api key'), 0)

if __name__ == '__main__':
    unittest.main()