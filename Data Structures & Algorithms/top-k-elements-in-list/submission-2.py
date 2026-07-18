class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        arr = []
        for key, count in counts.items():
            heapq.heappush(arr, (count, key))
            if len(arr) > k:
                heapq.heappop(arr)
        
        freq = []
        while arr:
            freq.append(heapq.heappop(arr)[1])
        
        return freq
