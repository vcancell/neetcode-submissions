class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, m = 0, 0
        for x in nums:
            if x == 1:
                curr += 1
            else:
                curr = 0
            m = max(m, curr)
        return m