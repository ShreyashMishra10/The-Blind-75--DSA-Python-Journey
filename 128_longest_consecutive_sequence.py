from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest=0
        for i in num:
            if (i-1) not in num:
                initial=i
                count=1
                while initial+1 in num:
                    initial+=1
                    count+=1
                longest =max(longest, count)
        return longest