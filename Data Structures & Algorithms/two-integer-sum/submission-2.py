class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in map:
                j = map[diff]
                if i > j:
                    return [j,i]
                return [i, j]
            
            map[nums[i]] = i  
        