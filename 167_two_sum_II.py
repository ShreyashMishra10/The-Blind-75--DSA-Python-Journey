from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i <j:
            sum_current = numbers[i]+numbers[j]
            if sum_current==target:
                return [i+1, j+1]
            elif sum_current > target:
                j-=1
            else:
                i+=1
        return []