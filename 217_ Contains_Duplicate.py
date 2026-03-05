from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set=set()
        for i in nums:
            if i in new_set:
                return True
            new_set.add(i)
        else:
            return False
        