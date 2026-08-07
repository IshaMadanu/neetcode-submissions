class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        ans = []
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        sortDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            ans.append(list(sortDict)[i])
        
        return ans