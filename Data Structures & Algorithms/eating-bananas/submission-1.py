class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        minR, maxR = 1, piles[0]
        trueR = piles[0]
        while minR <= maxR:
            hours = 0
            currR = (maxR + minR ) // 2
            for b in piles:
                hours += math.ceil(b / currR)
                if hours > h:
                    minR = currR + 1
                    break
            if hours <= h:
                trueR = min(trueR, currR)
                maxR = currR - 1
        return trueR