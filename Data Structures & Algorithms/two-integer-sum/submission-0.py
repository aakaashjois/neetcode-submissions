class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, n in enumerate(nums):
            lookup = target - n
            if lookup in m:
                j = m[lookup]
                return [j, i]
            m[n] = i
