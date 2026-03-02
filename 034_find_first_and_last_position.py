from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def finding(search_left: bool) -> int:
            low = 0
            high = len(nums) - 1
            idx = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    idx = mid 
                    if search_left:
                        high = mid - 1 
                    else:
                        low = mid + 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return idx

        first = finding(True)
        last = finding(False)
        
        return [first, last]
