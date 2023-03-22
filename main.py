import random
import math
import time
import matplotlib.pyplot as plt
import numpy as np

def sieve_of_eratosthenes(n):
    nums = [False, False]
    nums += [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i]:
            j = 0
            while (i ** 2) + (j * i) <= n:
                nums[(i ** 2) + (j * i)] = False
                j += 1
    return nums

df = []

for i in range(10):
    start = time.time()

    sieve_of_eratosthenes(10 ** i)

    end = time.time()

    df.append(end - start)
    print("DONE: " + str(i + 1) + "/10")

print(df)

small_value = 1e-10
df = np.log10([x + small_value for x in df])

plt.plot(list(range(10)), df)

plt.xlabel("Power of 10")
plt.ylabel("Time for execute")
plt.title("Execute time for Sieve of Eratosthenes")
plt.show()

print(df)