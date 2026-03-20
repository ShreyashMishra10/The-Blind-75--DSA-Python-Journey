from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit=0
        for i in range(1, len(prices)):
            new_profit=prices[i]-prices[left]
            if prices[i] < prices[left]:
                left=i
            else:
                profit = max(new_profit, profit)
        return profit