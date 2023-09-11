import unittest
from bisection import bisect

# derive from unittest.TestCase
class TestIdentity(unittest.TestCase):

    # all methods that start with test are executed
    def testRoot(self):
        interval, root = bisect(lambda x: x, -1.2, 1.,tol=1.e-8)
        expected = 0.
        self.assertAlmostEqual(root , expected)

    # this method will be ignored
    def somethingelse(self):
        self.testRoot()

    # test expected failures
    @unittest.expectedFailure
    def testInterval(self):
        interval, root = bisect(lambda x: x, -1.2, -0.5,tol=1.e-8)
        expected = 0.
        self.assertAlmostEqual(root , expected)

    # we expect failure here because the number of iterations is not large enough
    @unittest.expectedFailure
    def testIterations(self):
        interval, root = bisect(lambda x: x, -1.2, -0.5,tol=1.e-8, maxit=2)
        expected = 0.
        self.assertAlmostEqual(root , expected)

if __name__== '__main__':
    unittest.main ()
