class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        count = 0
        for elem in nums:
            if elem == 1:
                count += 1
            else:
                count = 0
            maxNum = max(maxNum, count)
        return maxNum