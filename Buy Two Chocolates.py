from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total_cost = prices[0] + prices[1]
        
        if total_cost <= money:
            return money - total_cost
        return money
