class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm, rm = 0, len(matrix) - 1

        while lm <= rm:
            mm = (rm + lm) // 2
            if target >= matrix[mm][0] and target <= matrix[mm][len(matrix[0]) - 1]:
                ln, rn = 0, len(matrix[0]) - 1
                while ln <= rn:
                    mn = (rn + ln) // 2
                    if target > matrix[mm][mn]:
                        ln = mn + 1
                    elif target < matrix[mm][mn]:
                        rn = mn - 1
                    else:
                        return True
                return False
            elif target > matrix[mm][0]:
                lm = mm + 1
            elif target < matrix[mm][0]:
                rm = mm - 1
        return False