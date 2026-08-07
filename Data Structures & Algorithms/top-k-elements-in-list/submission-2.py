class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #bucket sort:
        # index = count; values = num in nums
        # return last k indices
        myDict = {}
        freq = [[]for i in range(len(nums) + 1)]

        for num in nums:
            myDict[num] = 1 + myDict.get(num, 0) #0 if doesnt exist
        for num, count in myDict.items():
            freq[count].append(num) #num occurs count amt of items
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans




## sorting adds non-optimal time
# myDict = {}
# ans = []
# for num in nums:
#     if num in myDict:
#         myDict[num] += 1
#     else:
#         myDict[num] = 1
# sortDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))
# for i in range(k):
#     ans.append(list(sortDict)[i])

# return ans