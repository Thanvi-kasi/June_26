class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                count = 0
                curr = i

                while not visited[curr]:
                    visited[curr] = True
                    curr = nums[curr]
                    count += 1

                ans = max(ans, count)

        return ans
