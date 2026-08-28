class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            if nums[0] + nums[1] == target:
                return [0, 1]
        visited = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if nums[i] not in visited:
                visited[difference] = i
            else:
                return [visited[nums[i]], i]
            
        # for val in visited.values():
        #     if len(val) == 2:
        #         i = val[0]
        #         j = val[1]
        #         if visited[i] + visited[j] == target:
        #             return [i, j]
        #     return []
        
        

            

            
            
            


        
        