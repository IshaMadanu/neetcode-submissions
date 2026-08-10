class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O n time and space
        #list of lists store freq output > count, num
        # dict; key = count; value = num in nums
        # each list within holds values

        myList = [[] for _ in range(len(nums) + 1)]
        myDict = {}
        ans = []
        for num in nums:
            myDict[num] = 1 + myDict.get(num, 0)
        for num, count in myDict.items():
            myList[count].append(num)

        for i in range(len(myList) - 1, 0, -1):
            for num in myList[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans