class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = heights[0]
        stack = []
        limits = [len(heights)] * len(heights)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                limits[stack[-1]] = i
                stack.pop(-1)
            stack.append(i)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                r = limits[stack[-1]] - 1
                l = i + 1
                maxArea = max(maxArea, heights[stack.pop(-1)] * (r - l + 1))
            stack.append(i)
        for i in stack:
            maxArea = max(maxArea, heights[i] * (limits[i] -1 - 0 + 1))
            
        return maxArea

