class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        curr = 1 if nums else 0
        m = max(0, curr)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr += 1
            elif nums[i] != nums[i - 1]:
                curr = 1
            m = max(m, curr)
        return m