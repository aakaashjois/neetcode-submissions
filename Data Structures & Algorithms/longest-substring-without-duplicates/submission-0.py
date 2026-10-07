class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        i = 0
        j = 1
        
        seen = set()
        seen.add(s[i])

        length = len(seen)

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                length = max(len(seen), length)
                j += 1
        
        return length
            