class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        myDict = {}
        ans = []

        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        for num, count in myDict.items():
            freq[count].append(num)

        for i in range (len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
