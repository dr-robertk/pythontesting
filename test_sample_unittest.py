import unittest

from test_sample import func

class TestSample(unittest.TestCase):

    # test 1
    def test_func(self):
        self.assertEqual(func(3), 4)

    # test 2
    @unittest.expectedFailure
    def test_func2(self):
        self.assertFalse(func(2), 4)

if __name__ == '__main__':
    unittest.main()
