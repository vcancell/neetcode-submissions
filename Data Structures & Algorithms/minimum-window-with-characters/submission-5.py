class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_freqs = {}
        s_freqs = {}
        l = 0
        res = ""

        for c in t:
            t_freqs[c] = 1 + t_freqs.get(c, 0)

        for r in range(len(s)):
            s_freqs[s[r]] = s_freqs.get(s[r], 0) + 1
            if any(s_freqs.get(c, 0) < t_freqs[c] for c in t_freqs):
                continue
            while s_freqs[s[l]] > t_freqs.get(s[l], 0):
                s_freqs[s[l]] = s_freqs[s[l]] - 1
                l += 1
            res = res if len(res) <= (r - l) + 1 and res else s[l:r + 1]
            
        return res
