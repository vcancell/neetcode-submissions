class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                left, height = stack.pop()
                maxArea = max(maxArea, height * (i - left))
                start = left
            stack.append((start, h))
        for (l, h) in stack:
            maxArea = max(maxArea, h * (len(heights) - l))  
        return maxArea
