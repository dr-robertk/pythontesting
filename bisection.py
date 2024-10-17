import numpy as np

# a simple bisection algorithm
def bisect(f, a, b, tol = 1e-8, maxit=100):

    mid = np.inf
    if f(a)*f(b) < 0.:
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
    return [a, b], mid
