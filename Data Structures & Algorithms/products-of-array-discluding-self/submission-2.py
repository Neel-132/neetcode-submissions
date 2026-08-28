class Solution:
    def get_array_product(self, nums:List[int]):
        product = 1
        product_non_zero = 1
        non_zero_flag = False
        count = 0
        if len(nums) == 0:
            return 0, 0
        if len(nums) == 1:
            return nums[0], nums[0]
        for num in nums:
            if num == 0:
                count += 1
                product *= num
                continue
            non_zero_flag = True
            product *= num
            product_non_zero *= num
        if not non_zero_flag or count > 1:
            product_non_zero = 0
        return product, product_non_zero

    def productExceptSelf(self, nums: List[int]) -> List[int]:
          product, product_non_zero = self.get_array_product(nums)
          return [product // nums[i] if nums[i] != 0 else product_non_zero for i in range(len(nums)) ]