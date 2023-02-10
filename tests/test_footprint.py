import os
import unittest

success_exit_codes = [0]
error_exit_codes = [1, 256]

class TestFootprint(unittest.TestCase):
    def testFootprint(self):
        # Test that running footprint with no arguments returns an exit code, as well as creates a config file
        self.assertIn(os.system('python -m footprint'), success_exit_codes)
        self.assertTrue(os.path.exists('./footprint/.conf'))
        # Test that running footprint with an email returns an exit code
        self.assertIn(os.system('python -m footprint example@example.com'), success_exit_codes)
        # Test that running footprint set with a valid <api> and a <key> returns an exit code
        self.assertIn(os.system('python -m footprint set hunter hunterapikey'), success_exit_codes)
        # Test that running footprint set with an invalid <api> and a <key> returns a 1 exit code
        self.assertIn(os.system('python -m footprint set invalid ApiKey'), error_exit_codes)

if __name__ == '__main__':
    unittest.main()