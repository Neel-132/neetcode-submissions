class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not isinstance(nums, list) or len(nums) == 1:
            return False 
        return len(set(nums)) < len(nums)