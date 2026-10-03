class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = defaultdict(int)
        t_d = defaultdict(int)

        for c in s:
            s_d[c] += 1
        for c in t:
            t_d[c] += 1
        
        return s_d == t_d
    