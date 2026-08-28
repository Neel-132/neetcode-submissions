class Solution:
    def get_area(self, length, breadth):
        return length * breadth
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while(i < j):
            min_length = min(heights[i], heights[j])
            area = self.get_area(j - i, min_length)
            if max_area < area:
                max_area = area
            if heights[i] == min_length:
                i += 1
            if heights[j] == min_length:
                j -= 1

        return max_area
        