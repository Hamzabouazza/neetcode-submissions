class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freqElement = defaultdict(int)

        
        for num in nums:
            freqElement[num] += 1
        
        for num, freq in freqElement.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for freq, num in heap:
            res.append(num)
        return res
            

        


        