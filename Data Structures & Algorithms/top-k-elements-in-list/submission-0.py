class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        freq = [count[1] for count in heap]
        return freq