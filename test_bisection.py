# import the pytest module use with the below tests
import pytest

# modules that need to be installed should be listed in requirements.txt
import numpy as np

# this will fail unless in requirements.txt
# import scipy

from bisection import bisect

def test_root():
    tol = 1.e-8
    interval, root = bisect(lambda x: x, -1.2, 1.,tol=tol)
    assert abs(root) <= tol

def root_param(a, b, maxit):
    tol = 1.e-8
    interval, root = bisect(lambda x: x, a, b,tol=tol, maxit=maxit)
    return root

# use parameterize decorators to test different parameter sets
@pytest.mark.parametrize("inpt, exptd", [((-1.2, 1, 100), 0),
                                         ((-1.2, 1, 10), 0.000976562), # no convergence in 10 its
                                         ((-2, -1, 100), np.inf)])
def test(inpt, exptd):
    root = root_param(*inpt)
    if not np.isinf( exptd ):
        assert np.abs(root - exptd) < 1e-8
    else:
        assert np.isinf( root )
