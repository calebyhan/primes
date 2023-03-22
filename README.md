Different methods of handling prime numbers. Most sources are credited to Wikipedia and appropiately following sources. All code used is by no means perfectly optimized, and all data shown should be merely used as reference.

## Finding

### [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

This method of finding primes is perhaps the most famous, as it is simple yet clever. As you iterate through each integer from 2 to $\sqrt{n}$, you eliminate its multiples. The time complexity is $O(n \log{\log{n}})$.

A sample pseudocode is as follows:

```
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n
        if A[i] is true
            for j = i², i²+i, i²+2i, i²+3i, ..., not exceeding n
                set A[j] := false

    return all i such that A[i] is true.
```

![Sieve of Eratosthenes](https://cdn.discordapp.com/attachments/905301278647783428/1087886676954722304/image.png)

| Power | Time (seconds)        |
| ----- | --------------------- |
| 0     | 0.0 (negligible)      |
| 1     | 0.0 (negligible)      |
| 2     | 0.0 (negligible)      |
| 3     | 0.0009982585906982422 |
| 4     | 0.006980419158935547  |
| 5     | 0.07981514930725098   |
| 6     | 0.8839259147644043    |
| 7     | 9.926632642745972     |
| 8     | 105.78479337692261    |
| 9     | 1128.1615352630615    |

| Power | Log Time (log seconds) |
| ----- | ---------------------- |
| 0     | -10.0                  |
| 1     | -10.0                  |
| 2     | -10.0                  |
| 3     | -3.0007569             |
| 4     | -2.15611849            |
| 5     | -1.09791467            |
| 6     | -0.05358413            |
| 7     | 0.99680195             |
| 8     | 2.02442324             |
| 9     | 3.05237129             |


### [Sieve of Sundaram](https://en.wikipedia.org/wiki/Sieve_of_Sundaram)

This more recent method is a variant of the Sieve of Eratosthenes. We first take a list of numbers from 1 to n. We then remove all numbers in the form $i + j + 2ij$ where:
* $i,j\in\mathbb{N},\ 1 \le i \le j$
* $i + j + 2ij \le n$

Then, we are left with all primes to 2n + 2 (except for 2) when multiplying the remaining numbers and adding 1.

A sample pseudocode is as follows:

```
algorithm Sieve of Sundaram is
    input: an integer n > 1.
    output: all prime numbers from 3 through 2n + 2.

    handle if n is less than 3

    let k be (n - 3) // 2 + 1

    let A be an array of Boolean values, indexed by integers 1 to n, initially all set to true.
    
    let i, j be equal to 1

    for i = 0, 1, 2, 3, ..., not exceeding (√n - 3) // 2 + 1
        for j 


    return all i such that A[i] is true.
```

## Checking

asd


## Nth prime

asd