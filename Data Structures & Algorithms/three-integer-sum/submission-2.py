class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]: #not first value and not reusing prev value
                continue
            left = index + 1
            right  = len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ans
