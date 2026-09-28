class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for _s in s:
            s_dict[_s] += 1
        t_dict = defaultdict(int)
        for _t in t:
            t_dict[_t] += 1
        return s_dict == t_dict