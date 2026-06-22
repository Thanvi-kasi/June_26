class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def max_subsequence(nums: List[int], k: int) -> List[int]:
            drop = len(nums) - k
            stack = []

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:k]

        def greater(a: List[int], i: int, b: List[int], j: int) -> bool:
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1

            if j == len(b):
                return True
            if i == len(a):
                return False

            return a[i] > b[j]

        def merge(a: List[int], b: List[int]) -> List[int]:
            i = j = 0
            res = []

            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1

            return res

        m, n = len(nums1), len(nums2)
        ans = [0] * k

        for i in range(max(0, k - n), min(k, m) + 1):
            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)

            candidate = merge(part1, part2)

            if greater(candidate, 0, ans, 0):
                ans = candidate

        return ans
