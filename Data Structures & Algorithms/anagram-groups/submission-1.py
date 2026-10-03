class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = defaultdict(list)
        for s in strs:
            hashes[tuple(sorted(s))].append(s)
        return list(hashes.values())
