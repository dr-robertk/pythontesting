from numpy import array, arange
from numpy import sum as npsum

import timeit

# use timeit and repeat to time small code snippets
def getTime(stmt, setup, N = 100):
    s = timeit.repeat(stmt=stmt, setup=setup, number=1, repeat=N, globals=globals())
    # return average, min, max
    return sum(s)/N, min(s), max(s)

idx = [10,100,1000,10000, 100000]
def doLoop(stmt):
    s_time = list()
    for i in idx:
        setup = 'a=array(arange(0,'+str(i) + '))'
        times = getTime(stmt, setup)
        s_time.append(times[0])
    return s_time

# compute sum using default sum function
s = doLoop('sum(a)')
# compute sum using numpy sum function
n = doLoop('npsum(a)')

print(s)
print(n)

from matplotlib.pyplot import *

plot(idx, s, "--", label="sum")
plot(idx, n, "-", label="np.sum")
legend()
show()
