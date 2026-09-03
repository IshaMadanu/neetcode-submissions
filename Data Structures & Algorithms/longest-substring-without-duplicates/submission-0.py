class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        table = {}

        while right < len(s):
            table[s[right]] = table.get(s[right], 0) + 1

            while table[s[right]] > 1:
                table[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
            
