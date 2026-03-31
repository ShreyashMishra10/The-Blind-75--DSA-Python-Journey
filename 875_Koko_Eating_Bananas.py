from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high= max(piles)
        res = high

        while low <= high:
            k = (low+high)//2
            total_hrs= 0
            for i in piles:
                total_hrs += (i+k-1)//k
            if total_hrs <=h :
                res = k
                high = k-1
            else:
                low = k+1
        return res