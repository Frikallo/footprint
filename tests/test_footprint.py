import os
import unittest

ERROR_CODE_LIN = 256
ERROR_CODE_WD = 1
SUCCESS_CODE = 0

class TestFootprint(unittest.TestCase):
    def testFootprint(self):
        # Test that running footprint with no arguments returns a 1 exit code, as well as creates a config file
        self.assertEqual(os.system('python -m footprint'), SUCCESS_CODE)
        self.assertTrue(os.path.exists('./footprint/.conf'))
        # Test that running footprint with an email returns a 200 exit code
        self.assertEqual(os.system('python -m footprint example@example.com'), SUCCESS_CODE)
        # Test that running footprint set with a valid <api> and a <key> returns a 200 exit code
        self.assertEqual(os.system('python -m footprint set hunter ApiKey'), SUCCESS_CODE)
        # Test that running footprint set with an invalid <api> and a <key> returns a 0 or 256 exit code
        self.assertIn(os.system('python -m footprint set invalid ApiKey'), [ERROR_CODE_LIN, ERROR_CODE_WD])

if __name__ == '__main__':
    unittest.main()