class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            a = (j - i) * min(heights[i], heights[j])
            if a > area:
                area = a
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return area