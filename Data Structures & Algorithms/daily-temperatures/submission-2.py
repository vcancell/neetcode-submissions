class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for r in range(len(temperatures)):
            temp = temperatures[r]
            while stack and temperatures[stack[-1]] < temp:
                result[stack[-1]] = r - stack[-1]
                stack.pop(-1)
            stack.append(r)
        return result