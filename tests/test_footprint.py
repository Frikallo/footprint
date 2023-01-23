import os
import unittest

accepted_exit_codes = [0, 1, 256]

class TestFootprint(unittest.TestCase):
    def testFootprint(self):
        # Test that running footprint with no arguments returns a exit code, as well as creates a config file
        self.assertIn(os.system('python -m footprint'), accepted_exit_codes)
        self.assertTrue(os.path.exists('./footprint/.conf'))
        # Test that running footprint with an email returns a exit code
        self.assertIn(os.system('python -m footprint example@example.com'), accepted_exit_codes)
        # Test that running footprint set with a valid <api> and a <key> returns a exit code
        self.assertIn(os.system('python -m footprint set hunter hunterapikey'), accepted_exit_codes)
        # Test that running footprint set with an invalid <api> and a <key> returns a 0 or 256 exit code
        self.assertIn(os.system('python -m footprint set invalid ApiKey'), accepted_exit_codes)

if __name__ == '__main__':
    unittest.main()