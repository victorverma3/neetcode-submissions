class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = defaultdict(int)
        right = defaultdict(int)

        curr = 1
        for i in range(len(nums)):
            left[i] = curr
            curr = curr * nums[i]
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = curr
            curr = curr * nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])

        return res