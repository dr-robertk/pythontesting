import numpy as np
from line_profiler import profile

# a simple bisection algorithm
@profile
def bisect(f: callable,
           a : float,
           b : float,
           tol : float = 1e-8,
           maxit : int = 100) -> tuple:

    for i in range(maxit):
        mid = 0.5 * (a+b)
        # check if result is good enough
        if abs(b-a) < tol:
            return [a, b], mid

        if f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid

    # iteration failed within number of allowed iterations
    return [a, b], np.inf

if __name__ == '__main__':
    bisect(lambda x: (x+1)*x, -1, 1)
    bisect(lambda x: np.exp(x)-1, -1, 1)
    bisect(lambda x: 4 - x, 2, 6 )
