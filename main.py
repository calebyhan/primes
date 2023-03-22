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


def sieve_of_sundaram(n):
    if n < 3:
        if n < 2:
            return 0
        else:
            return 1    
    k = (n - 3) // 2 + 1

    nums = [True for i in range(k)]

    for i in range((int(math.sqrt(n)) - 3) // 2 + 1):
            p = 2 * i + 3
            s = (p * p - 3) // 2

            for j in range(s, k, p):
                nums[j] = False
    return nums

df = []

for i in range(10):
    start = time.time()

    sieve_of_sundaram(10 ** i)

    end = time.time()

    df.append(end - start)
    print("DONE: " + str(i + 1) + "/10")

print(df)

small_value = 1e-10
df = np.log10([x + small_value for x in df])

plt.plot(list(range(10)), df)

plt.xlabel("Power of 10")
plt.ylabel("Time for execute")
plt.title("Execute time for Sieve of Sundaram")
plt.show()

print(df)