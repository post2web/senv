import unittest
from senv import Senv

class SenvTestCase(unittest.TestCase):
    """Tests for `senv.py`."""

    def test_default(self):
        Senv.change_name('test_case')
        self.assertTrue(len(Senv) == 0)
        Senv['a'] = 1
        Senv['b'] = '2'
        self.assertTrue(len(Senv) == 2)



if __name__ == '__main__':
    unittest.main()
