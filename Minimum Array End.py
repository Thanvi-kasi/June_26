class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        k = n - 1
        bit = 0

        while k:
            if ((x >> bit) & 1) == 0:
                if k & 1:
                    ans |= (1 << bit)
                k >>= 1
            bit += 1

        return ans
