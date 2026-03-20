class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        left=0
        count=0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[left])
                left+=1
            window.add(s[i])
            current_count = i - left + 1
            count = max(count, current_count)
        return count