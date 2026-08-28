class Solution:
    def get_prefix_max(self, height:List[int]):
        prefix_max = [0] * len(height)
        prefix_max[0] = height[0]
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
        return prefix_max


    def get_suffix_max(self, height:List[int]):
        suffix_max = [0] * len(height)
        suffix_max[-1] = height[-1]
        n = len(height) - 1
        for i in range(1, len(height)):
            suffix_max[n - i] = max(suffix_max[n - i + 1], height[n - i])
        return suffix_max

    def trap(self, height: List[int]) -> int:
        total_water = 0
        prefix_max = self.get_prefix_max(height)
        suffix_max = self.get_suffix_max(height)
        
        for item in range(len(height)):
            left_max = prefix_max[item]
            right_max = suffix_max[item]
            if height[item] != min(left_max, right_max):
                total_water += min(left_max, right_max) - height[item]
            else:
                continue
        return total_water


        
        