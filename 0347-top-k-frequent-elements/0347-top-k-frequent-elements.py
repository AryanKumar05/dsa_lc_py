import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap=[]
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num,count in freq.items():
            heapq.heappush(minheap,(count,num))
            if len(minheap)>k:
                heapq.heappop(minheap)
        return [num for count,num in minheap]
        



        