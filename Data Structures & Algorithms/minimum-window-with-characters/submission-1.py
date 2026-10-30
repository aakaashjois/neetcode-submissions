class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_c = defaultdict(int)
        for c in t:
            t_c[c] += 1
        
        remaining = len(t)
        min_length = sys.maxsize
        substring = ""

        l = 0
        for r in range(len(s)):
            if s[r] in t_c:
                if t_c[s[r]] > 0:
                    remaining -= 1
                t_c[s[r]] -= 1
            
            while remaining == 0:
                if r - l + 1 < min_length:
                    substring = s[l : r + 1]
                    min_length = r - l + 1
                if s[l] in t_c:
                    t_c[s[l]] += 1
                    if t_c[s[l]] > 0:
                        remaining += 1
                l += 1
        
        return substring

        

