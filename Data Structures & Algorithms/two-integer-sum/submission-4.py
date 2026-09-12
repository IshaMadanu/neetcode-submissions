class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict stores key= difference between number and the target, value = index of number in nums,
        # if a value in dictionary, a difference, is already in the dict, return that differences index, and the index of curr number 
        #else, add num + index to dict, to find if next diff is in dict

        d = {}

        for ind, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], ind]
            d[num]  = ind
        return []