import unittest

from file import getCompleteTemplate

class TestSum(unittest.TestCase):
    def test_template(self):
        """
        Test that it can sum a list of integers
        """
        schemas = []
        getCompleteTemplate(schemas,"templates", "cutter", "v0.1", "cutter")
        print(schemas)

if __name__ == '__main__':
    unittest.main()