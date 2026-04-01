from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res=high
        while low <= high:
            capacity = (low+high)//2
            if self.can_ship(weights, days, capacity):
                res= capacity
                high=capacity-1
            else:
                low = capacity +1
        return res
    def can_ship(self, weights, days, cap):
        ships_used = 1
        current_load = 0
        for w in weights:
            if current_load + w > cap:
                ships_used += 1
                current_load = 0
            current_load += w
        return ships_used <= days
