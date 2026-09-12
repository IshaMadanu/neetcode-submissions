class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False

        for char in s:
            sDict[char] = sDict.get(char, 0) + 1

        for char in t:
            tDict[char] = tDict.get(char, 0) + 1
        
        for key in sDict:
            if key not in tDict or tDict[key] != sDict[key]:
                return False

        return True