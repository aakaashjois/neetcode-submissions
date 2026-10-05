class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strings = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[j:i])
                string = s[i + 1:i + 1 + length]
                strings.append(string)
                i = j = i + length + 1
            else:
                i += 1
        return strings