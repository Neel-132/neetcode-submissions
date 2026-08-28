class Solution:
    def prefix_suffix_product(self, nums:List[int]):
        prefix_prod = []
        suffix_prod = []
        pref_prod = nums[0]
        suff_prod = nums[-1]
        for i in range(len(nums)):
            if i > 0:
                pref_prod *= nums[i]
            prefix_prod.append(pref_prod)

        for j in range(len(nums) - 1, -1, -1):
            if j < len(nums) - 1:
                suff_prod *= nums[j]
            suffix_prod.append(suff_prod)
        return prefix_prod, suffix_prod
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, suffix_prod = self.prefix_suffix_product(nums)
        prod_except_self = []
        print("P ",prefix_prod)
        print("Q ", suffix_prod)
        n = len(nums)
        for i in range(n):
            if i == 0:
                prod_except_self.append(suffix_prod[n - 2])
            elif i == (n - 1):
                prod_except_self.append(prefix_prod[n - 2])
            else:
                product_except_self = prefix_prod[i - 1] * suffix_prod[n - i - 2]
                prod_except_self.append(product_except_self)
        return prod_except_self





