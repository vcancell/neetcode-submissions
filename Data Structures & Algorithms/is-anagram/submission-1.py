class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # if len(s) != len(t):
        #     return False
        
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False
        # return True

        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True