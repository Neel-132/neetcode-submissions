class Solution:
    def trap(self, height:List[int]):
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        total = 0
        while(l < r):
           
            if l_max <= r_max:
                if height[l] < l_max:
                    total += (l_max - height[l])
                    l += 1
                else:
                    l_max = height[l]
                    if l_max > r_max:
                        r -= 1
                    else:
                        l += 1
            else:
                if height[r] < r_max:
                    total += (r_max - height[r])
                    r -= 1
                else:
                    r_max = height[r]
                    if l_max > r_max:
                        r -= 1
                    else:
                        l += 1

        return total