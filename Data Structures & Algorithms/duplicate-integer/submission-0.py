class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for num in nums:
            if num in ht:
                return True
            else:
                ht[num] = 1
        return False
