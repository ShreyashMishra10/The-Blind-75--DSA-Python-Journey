class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count={}
        for i in t:
            t_count[i] = 1+t_count.get(i, 0)
        window ={}
        have, want = 0, len(t_count)    
        res, res_len = [-1,-1], float('inf')
        left=0
        for j in range(len(s)):
            window[s[j]]=1+window.get(s[j],0)
            if s[j] in t_count and window[s[j]] == t_count[s[j]]:
                have+=1
            while have==want:
                if (j-left+1)<res_len:
                    res=[left, j]
                    res_len=j-left+1
                window[s[left]]-=1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have-=1
                left+=1
        l,r=res
        return s[l: r+1] if res_len!=float('inf') else ""