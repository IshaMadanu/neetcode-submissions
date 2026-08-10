class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            sDict[char] = 1 + sDict.get(char, 0)
        for char in t:
            tDict[char] = 1 + tDict.get(char, 0)

        for key in sDict:
            if key not in tDict or sDict[key] != tDict[key]:
                return False
        return True