# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, r = 0, n - 1
        peak = 0
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0:
                l = mid + 1
            elif mid == n - 1:
                r = mid - 1
            else:
                curr = mountain_arr.get(mid)
                nxt = mountain_arr.get(mid + 1)
                if curr < nxt:
                    l = mid + 1
                else:
                    peak = mid
                    r = mid - 1
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = peak + 1, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1