from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)

        ugly = [1] * n
        idx = [0] * k
        next_val = primes[:]

        for i in range(1, n):
            mn = min(next_val)
            ugly[i] = mn

            for j in range(k):
                if next_val[j] == mn:
                    idx[j] += 1
                    next_val[j] = primes[j] * ugly[idx[j]]

        return ugly[-1]
