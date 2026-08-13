class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                #isAlphaNum ensures its a string num/letter 
                #instead of . , or space
                left += 1
            while right > left and not self.isAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isAlphaNum(self, char):
        return ((ord('A') <= ord(char) <= ord('Z')) or
            (ord('a') <= ord(char) <= ord('z')) or
            (ord('0') <= ord(char) <= ord('9')))