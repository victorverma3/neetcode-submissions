class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = defaultdict(int)
        for index, num in enumerate(nums):
            diff = target - num
            if diff in ind:
                return [ind[diff], index]
            ind[num] = index
        
            