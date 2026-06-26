class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()

        score = 0
        rows = len(nums)
        cols = len(nums[0])
      
        for j in range(cols):
            mx = 0
            for i in range(rows):
                mx = max(mx, nums[i][j])
            score += mx

        return score
