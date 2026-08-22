class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in unique:
                continue
            count = 0
            curr = num
            while curr in unique:
                count += 1
                curr += 1
            longest = max(longest, count)
        
        return longest