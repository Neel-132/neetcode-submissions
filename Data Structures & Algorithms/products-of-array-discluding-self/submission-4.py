class Solution:
    def getprefixproduct(self, nums:List[int]):
        result = []
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            result.append(prefix)

        return result
    
    def getsuffixproduct(self, nums:List[int]):
        result = [1] * (len(nums) - 1)
        suffix = 1
        if len(nums) == 2:
            result[0] = nums[1]
            return result
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            result[i] = suffix

        return result
 
            
        

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.getprefixproduct(nums)
        suffix = self.getsuffixproduct(nums)
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix[i])
            elif i == (len(nums) - 1):
                result.append(prefix[i - 1])
            else:
                result.append((prefix[i - 1] * suffix[i]))

        return result

        