class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = [0] * 1001

        for num in arr1:
            freq[num] += 1

        ans = []

        for num in arr2:
            ans.extend([num] * freq[num])
            freq[num] = 0

        for num in range(1001):
            if freq[num]:
                ans.extend([num] * freq[num])

        return ans
