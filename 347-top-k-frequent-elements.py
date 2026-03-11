from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num={}
        for i in nums:
            num[i]=1+num.get(i, 0)
        list_pair=list(num.items())

        list_pair.sort(key=lambda item: item[1], reverse=True)

        res=[]
        for i in range(k):
            res.append(list_pair[i][0])
        return res