class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            left, right = 0, m - 1
            idx = m
            
            while left <= right:
                mid = left + (right - left) // 2
                if spell * potions[mid] >= success:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            pairs.append(m - idx)
            
        return pairs