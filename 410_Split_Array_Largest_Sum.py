class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(max_sum):
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True

        left = max(nums)
        right = sum(nums)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            if canSplit(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res