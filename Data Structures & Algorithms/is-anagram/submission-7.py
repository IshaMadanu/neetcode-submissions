class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26 # array of 26 spots

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
            #add then subtract when char same

        for key in count:
            if key != 0:
                return False
        return True