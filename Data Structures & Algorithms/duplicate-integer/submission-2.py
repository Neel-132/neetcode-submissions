class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_map = defaultdict(int)
        for item in nums:
            frequency_map[item]+= 1
            if frequency_map[item] > 1:
                return True
        
        return False
        