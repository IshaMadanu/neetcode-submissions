class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            mySum = numbers[left] + numbers[right]
            if mySum < target:
                left += 1
            elif mySum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []