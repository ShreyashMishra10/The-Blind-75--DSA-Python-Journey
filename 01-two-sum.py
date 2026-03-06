from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num:
                return [num[diff], i]
            num[n] = i