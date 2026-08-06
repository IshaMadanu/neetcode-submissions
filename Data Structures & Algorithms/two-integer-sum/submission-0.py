class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        ans = []
        for ind, num in enumerate(nums):
            diffKey = target - num

            if diffKey in myDict:
                ans.append(myDict[diffKey])
                ans.append(ind)
            myDict[num] = ind
        return ans