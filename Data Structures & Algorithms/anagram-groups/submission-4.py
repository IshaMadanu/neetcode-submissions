class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(m*n) time O(m) space; m = num strings, n = len of longest string

        # dict; key = array of letters 0-26, value = appended strings

        myDict = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for char in s:
                arr[ord(char) - ord('a')] += 1
            myDict[tuple(arr)].append(s)
        
        return list(myDict.values())
