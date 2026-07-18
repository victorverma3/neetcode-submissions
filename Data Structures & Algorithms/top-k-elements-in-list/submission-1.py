class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        arr = []
        for key, count in counts.items():
            heapq.heappush(arr, (-1 * count, key))
        
        freq = []
        for i in range(k):
            freq.append(heapq.heappop(arr)[1])
        
        return freq
