class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = float('-inf')

        for i in range(n):
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i]
            if dq:
                dp[i] += max(0, dp[dq[0]])

            ans = max(ans, dp[i])

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return ans
