class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #hold pair (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #while stack not empty and stacks latest elem's height is greater than curr height
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i - index)) #curr i - starting index
                start = index #move start to popped
            stack.append((start, h))

        for i, h in stack: #rects still left
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
