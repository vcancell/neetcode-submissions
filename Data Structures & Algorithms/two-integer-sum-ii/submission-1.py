class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = numbers[i]
            l = i + 1
            r = len(numbers) - 1
            t = target - x
            while l <= r:
                m = (r + l) // 2
                mnum = numbers[m]
                if mnum == t:
                    if i != m:
                        return [i + 1, m + 1]
                    # else:
                    #     l = (l + m) // 2
                    #     r = (r + m) // 2
                elif mnum < t:
                    l = m + 1
                else:
                    r = m - 1
        return [-1, -1] #Obvious: case will not be reached due to constraint: target exists