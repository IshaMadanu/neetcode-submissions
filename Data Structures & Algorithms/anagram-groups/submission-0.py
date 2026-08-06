class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for string in strs:
            myList = [0] * 26
            for char in string:
                myList[ord(char) - ord('a')] += 1
            myDict[tuple(myList)].append(string)

        return list(myDict.values())