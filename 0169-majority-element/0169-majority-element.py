from collections import Counter
import math
from typing import List
class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        limit=math.floor(len(nums)/2)
        obj=Counter(nums)
        return obj.most_common(1)[0][0]



        