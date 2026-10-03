class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Rules for anagram
        # 1. The strings are of same lengths
        # 2. The strings carry the same letters
        def string_hash(string: str):
            fixed = [0] * 26
            for c in string:
                fixed[ord(c) - ord('a')] += 1
            return tuple(fixed)

        hashes = dict()
        for s in strs:
            sh = string_hash(s)
            if sh in hashes:
                hashes[sh].append(s)
            else:
                hashes[sh] = [s]
        
        return list(hashes.values())
