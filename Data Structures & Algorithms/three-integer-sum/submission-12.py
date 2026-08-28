from typing import List
class Solution:
    def twosum(self, nums:List[int], target:int, i, j)-> List[int]:
        final_output = []
    
        while(i < j):
            if  len(final_output) > 0 and nums[i] == final_output[-1][0] and nums[j] == final_output[-1][1]:
                i += 1
                j -= 1
                continue
            
            elif (nums[i] + nums[j]) == target:
                final_output.append([nums[i], nums[j]])
                i += 1
                j -= 1
                continue

            elif nums[i] + nums[j] > target:
                j -= 1

            else:
                i += 1

        
        return final_output
            

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        end = len(nums) - 1
        for i in range(len(nums)):
            target = - nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if i < (len(nums) - 1):
                two_sum = self.twosum(nums, target, i + 1, end)
                if len(two_sum) > 0:
                    for pair in two_sum:
                        triplet = [nums[i]] + pair
                        answer.append(triplet)
            else:
                break
        return answer