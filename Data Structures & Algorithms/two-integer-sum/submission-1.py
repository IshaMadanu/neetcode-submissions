class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        myList = []
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in myDict:
                myList.append(myDict[diff])
                myList.append(ind)
            myDict[num] = ind
        return myList