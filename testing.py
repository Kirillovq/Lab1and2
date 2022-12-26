import unittest
from max import mel

class Testmel(unittest.TestCase):
    def test_mel(self):
        self.assertEqual(mel(6900), 9)

if __name__ == "__main__":
    unittest.main()