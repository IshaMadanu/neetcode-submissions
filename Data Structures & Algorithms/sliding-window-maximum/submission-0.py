class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        #max heap has elem = (vlaue, index)

        #add elem to heap, when windowsize == k: remove from heap if index is outside of curr window
        #top of heap = max for window

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i)) 
            #heapq is minheap, wnat max heap so -nums[i] > store nums as negs and then later when popping smallest, negate again to get positive greatest
            # adding neg value + index to heap

            if i >= k - 1:
                while heap[0][1] <= i - k: # if "smallest" val is outside window
                    #pop it
                    heapq.heappop(heap)
                
                res.append(-heap[0][0])
        return res




            # if index is enough for size k window:
                #need to remove index from left so
                #while heaps' min(our max)'s index is <= i - k
                #i - k is curr index - window size, so leave out everythign before
                    #pop old item outside of window
                #addthat neg min to our res, which is the max of that window
            