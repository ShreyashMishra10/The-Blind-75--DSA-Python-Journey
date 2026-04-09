class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        cand1, cand2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        n_third = len(nums) // 3
        for c in [cand1, cand2]:
            if nums.count(c) > n_third:
                result.append(c)
        return list(set(result))