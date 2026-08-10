class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) for both time/space
        myDict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in myDict:
                return [myDict[diff], index]
            myDict[num] = index

        #dict, key = numbers in num; value = index appeared
        #if difference in dict, then return diff/number's index + index