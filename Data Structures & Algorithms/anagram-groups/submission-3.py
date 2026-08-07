class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            myList = [0] * 26
            for char in s:
                myList[ord(char) - ord('a')] += 1
            myDict[tuple(myList)].append(s)
        return list(myDict.values())
