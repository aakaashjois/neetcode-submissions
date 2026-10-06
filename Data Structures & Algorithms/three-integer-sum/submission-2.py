class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)  # O(NLOG(N))
        results = []
        for i in range(len(snums)):
            if i > 0 and snums[i] == snums[i - 1]:
                continue
            j = i + 1
            k = len(snums) - 1
            t = -snums[i]
            while j < k:
                s = snums[j] + snums[k]
                if s == t:
                    results.append([snums[i], snums[j], snums[k]])
                    j += 1
                    k -= 1
                elif s < t:
                    j += 1
                elif s > t:
                    k -= 1
                while i + 1 < j < k and snums[j] == snums[j - 1]:
                    j += 1
                while j < k < len(snums) - 1 and snums[k] == snums[k + 1]:
                    k -= 1
        return results