class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join([char for char in s if char.isalnum()]).lower().replace(" ", "")
        # stack = []
        # l = len(s)
        # if l == 1:
        #     return True
        # for i in range(l):
        #     c = s[i]
        #     if not stack or (stack[-1] != c and (l % 2 != 1 or l // 2 != i)):
        #         stack.append(c)
        #     elif stack[-1] == c:
        #         stack.pop()
        # return not stack

        s = "".join([char for char in s if char.isalnum()]).lower().replace(" ", "")
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
