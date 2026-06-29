class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negatives = 0
        min_abs = float("inf")

        for row in matrix:
            for num in row:
                total += abs(num)
                if num < 0:
                    negatives += 1
                min_abs = min(min_abs, abs(num))

        if negatives % 2 == 0:
            return total
        return total - 2 * min_abs
