from numpy import array, arange
from numpy import sum as npsum

import time

a = array(arange(0,1000))

# default simple way of timing
start = time.time()

# commonly made mistake, use np.sum instead
# default sum implementation does not know about arrays
s = sum(a)

print(f"Standard sum took {time.time() - start:.6e} sec.")

start = time.time()

s = npsum(a)

print(f"Standard sum took {time.time() - start:6e} sec.")

