class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dict: key = num; value = difference needed
        # O(n) for both time/space
        myDict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in myDict:
                return [myDict[diff], index]
            myDict[num] = index