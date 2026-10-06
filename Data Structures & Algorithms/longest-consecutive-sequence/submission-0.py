class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set(nums) # O(N)
        longest = 1
        for num in nums:
            if num - 1 not in seen:
                length = 1
                i = num + 1
                while i in seen:
                    length += 1
                    i += 1
                if longest < length:
                    longest = length
        return longest