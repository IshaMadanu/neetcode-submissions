class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": #edge cases
            return ""
        result, resultLen = [-1, -1], float("infinity") 
        left = 0
        countT, currWindow = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        #keep count of have and need
        have, need = 0, len(countT)

        for right in range(len(s)): # right boundary of window table
            c = s[right]
            currWindow[c] = 1 + currWindow.get(c, 0) # add to window table

            if c in countT and currWindow[c] == countT[c]: #if right boundary is in t and if counts are the same
                have += 1
            
            while have == need: #condition met
                #update our result
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                #pop from left of currWindow
                currWindow[s[left]] -= 1
                if s[left] in countT and currWindow[s[left]] < countT[s[left]]: # if moving window makes currWindow counts < t's count
                    have -= 1
                left += 1  
        left, right = result
        if resultLen != float("infinity"):
            return s[left:right + 1]
        else:
            return ""




        # instead of comparing hashtables val/key, just comapre count

        # once have == need, string contains needed chars; store indicies as curr res + len
        #find shortest :
            # remove leftmost char until have is no longer == need