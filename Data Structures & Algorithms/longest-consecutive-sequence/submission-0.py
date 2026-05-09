class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for num in nums:
            if num - 1 not in seen:
                curr = num
                while curr + 1 in seen:
                    curr += 1
                longest = max(curr - num + 1, longest)
        
        return longest