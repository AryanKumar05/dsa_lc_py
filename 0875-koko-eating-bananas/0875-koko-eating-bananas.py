import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=1
        hi=max(piles)
        def can_finish(piles,k,h):
            hours_needed=0
            for pile in piles:
                if pile<=k:
                    hours_needed+=1
                else:
                    hours_needed+=math.ceil(pile/k)
            return hours_needed<=h
                
        while lo<hi:
            mid=lo+(hi-lo)//2
            if can_finish(piles,mid,h):
                hi=mid
            else:
                lo=mid+1
        return lo


        