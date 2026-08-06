class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False 

        for char in s:
            if char in sDict:
                sDict[char] = sDict[char] + 1
            else:
                sDict[char] = 1
        for char in t:
            if char in tDict:
                tDict[char] = tDict[char] + 1
            else:
                tDict[char] = 1
        
        for key in sDict:
            if key not in tDict:
                return False
            if sDict[key] != tDict[key]:
                return False

        return True
            