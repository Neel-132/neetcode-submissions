class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1 or not isinstance(nums, list):
            return False
        visited = set()
        for item in nums:
            if item not in visited:
                visited.add(item)
            else:
                return True
        return False