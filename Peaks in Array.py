from typing import List

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        class BIT:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)

            def update(self, i, delta):
                i += 1
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & -i

            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

            def range_query(self, l, r):
                if l > r:
                    return 0
                return self.query(r) - (self.query(l - 1) if l > 0 else 0)

        def is_peak(i):
            return 0 < i < n - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        bit = BIT(n)
        peak = [0] * n

        for i in range(1, n - 1):
            peak[i] = int(is_peak(i))
            if peak[i]:
                bit.update(i, 1)

        ans = []

        for typ, a, b in queries:
            if typ == 1:
                l, r = a, b
                ans.append(bit.range_query(l + 1, r - 1))
            else:
                idx, val = a, b

                for p in (idx - 1, idx, idx + 1):
                    if 0 < p < n - 1 and peak[p]:
                        bit.update(p, -1)

                nums[idx] = val

                for p in (idx - 1, idx, idx + 1):
                    if 0 < p < n - 1:
                        peak[p] = int(is_peak(p))
                        if peak[p]:
                            bit.update(p, 1)

        return ans
