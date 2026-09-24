class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r and nums[i] not in seen:
                lnum = nums[l]
                rnum = nums[r]
                t = lnum + rnum
                if t > -nums[i]:
                    while nums[r] == rnum and l < r:
                        r -= 1
                elif t < -nums[i]:
                    while nums[l] == lnum and l < r:
                        l += 1
                else:
                    result.append([nums[i], lnum, rnum])
                    while nums[r] == rnum and l < r:
                        r -= 1
                    while nums[l] == lnum and l < r:
                        l += 1
            seen.add(nums[i])
        return result