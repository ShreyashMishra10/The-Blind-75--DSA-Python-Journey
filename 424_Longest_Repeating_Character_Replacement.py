class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window={}
        max_frequency=0
        left=0
        max_length=0

        for i in range(len(s)):
            window[s[i]] = 1 + window.get(s[i], 0)

            max_frequency=max(max_frequency, window[s[i]])

            while (i - left + 1) - max_frequency > k : 
                window[s[left]]-=1
                left +=1

            max_length = max(max_length, (i - left + 1))
        
        return max_length