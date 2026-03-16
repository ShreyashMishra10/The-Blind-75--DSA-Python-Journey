from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sum_3=[]
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right=len(nums)-1
            while left<right:
                three_sum= nums[i]+nums[left]+nums[right]
                if three_sum==0:
                    sum_3.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif three_sum > 0:
                    right-=1
                else:
                    left+=1
        return sum_3
