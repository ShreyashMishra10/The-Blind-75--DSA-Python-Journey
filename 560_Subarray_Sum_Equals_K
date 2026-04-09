class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sums = {0: 1}
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
                    
        return count