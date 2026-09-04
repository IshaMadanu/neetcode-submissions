class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide window of len s1 over s2
        # for each check, check if char coutns are same in s1 and s2
        # char coutns in freq array

        if len(s1) > len(s2):
            return False
        
        count1, count2 = [0] * 26, [0] * 26

        for i in range(len(s1)): # window
            count1[ord(s1[i]) - ord('a')] += 1 #char index in 26, increment count
            count2[ord(s2[i]) - ord('a')] += 1
        
        match = 0

        for i in range(26):
            if count1[i] == count2[i]:
                match += 1
            else: 
                match += 0

        #move window and update counts
        left = 0
        for right in range(len(s1), len(s2)):
            if match == 26:
                return True
            
             # add right char
            index = ord(s2[right]) - ord('a')
            count2[index] += 1
            if count1[index] == count2[index]:
                match += 1
            elif count1[index] + 1 == count2[index]:
                match -= 1
            
            #subtract left char
            index = ord(s2[left]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                match += 1
            elif count1[index] - 1 == count2[index]:
                match -= 1

            left += 1

        return match == 26


        