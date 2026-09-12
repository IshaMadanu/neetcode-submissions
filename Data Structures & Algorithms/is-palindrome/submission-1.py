class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer from start and end
        # if char is not alpha num, index ++
        # if char left != char right: false

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isAlpha(s[left]):
                left += 1
            while right > left and not self.isAlpha(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    
    # method to classify whether char is alphanumeric or not
    def isAlpha(self, char):
        return ((ord('A') <= ord(char) <= ord('Z')) or
            (ord('a') <= ord(char) <= ord('z')) or
            (ord('0') <= ord(char) <= ord('9')))
        
        # true if ord of char is bwtn A-Z or a-z or 0-9