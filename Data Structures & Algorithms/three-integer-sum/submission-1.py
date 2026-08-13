class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1

            if num > 0:
                break
            if index > 0 and num == nums[index - 1]:
                continue

            while left < right:
                sum = num + nums[left] + nums[right]

                if sum > 0 : 
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return ans