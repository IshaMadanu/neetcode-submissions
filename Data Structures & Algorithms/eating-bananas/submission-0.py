class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        res = 0

        while low <= high:
            k = (low + high) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k) # add time it takes for each pile
            if totalTime <= h:
                res = k
                high = k - 1
            else:
                low = k + 1 #keep going to see if theres miinimum
        return res
            
            
        #x bananas/ k banana/hr = finish x bananas

        #find minimum value of k, for arr that is under h
        #upper bound for k = max(arr) bc if largest pile fits in an hr, then all else will
        #binary search: search values from low to high, where value/k = totalTime
            #ans = k if totalTime is less than h