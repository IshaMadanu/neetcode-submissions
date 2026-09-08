class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        low = 0
        high = len(nums) - 1

        while low <= high: #if curr window is already sorted, aka reach start, ans = nums[low]
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break

            mid = (low + high) // 2
            res = min(res, nums[mid]) #curr res = smallest val so far, use binary search to find
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1


        return res
