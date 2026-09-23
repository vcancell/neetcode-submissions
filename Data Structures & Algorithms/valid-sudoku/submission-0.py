class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                b = (r // 3) * 3 + (c // 3)
                curr = board[r][c]
                if curr in rows[r] or curr in cols[c] or curr in boxes[b]:
                    return False
                if curr == ".":
                    continue
                rows[r].add(curr)
                cols[c].add(curr)
                boxes[b].add(curr)
        return True