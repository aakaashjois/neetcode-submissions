class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix_height = [0] * len(height)
        suffix_height = [0] * len(height)

        for i in range(1, len(height)):
            prefix_height[i] = max(prefix_height[i - 1], height[i - 1])
        
        for j in range(len(height) - 2, -1 , -1):
            suffix_height[j] = max(suffix_height[j + 1], height[j + 1])
        
        output = 0
        for k in range(len(height)):
            water = min(prefix_height[k], suffix_height[k]) - height[k]
            if water > 0:
                output += water
        return output