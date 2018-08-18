import unittest
from count import count

class TestCase(unittest.TestCase):
    """Tests for `count.py`."""

    def test_is_five_prime(self):
        """Is apple successfully counted two times?"""
        self.assertTrue(2 == count("should find two apples. this is the second apple.", "apple"))

if __name__ == '__main__':
    unittest.main()
