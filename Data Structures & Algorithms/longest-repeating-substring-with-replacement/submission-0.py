class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        longest = 0

        table = {}

        highestCount = 0

        while right < len(s):
            table[s[right]] = table.get(s[right], 0) + 1
            highestCount = max(highestCount, table[s[right]])

            while (right - left + 1) - highestCount > k:
                table[s[left]] -= 1
                left += 1
                 # window size - highestCountof a char > k
                #characters that aren't most freq need to be replaced, so we get list of only XXXX or AAAAAAA
                # so while the window - good chars is greater than length needed (which is k)
            
            longest = max(longest, right - left + 1)
            right += 1

        return longest