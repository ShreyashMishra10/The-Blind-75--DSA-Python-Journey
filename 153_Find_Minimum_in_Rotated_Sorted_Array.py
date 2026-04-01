from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low <= high:
            if nums[low]>nums[high]:
                nums[low],nums[high]=nums[high],nums[low]
            high -=1
        return nums[0]