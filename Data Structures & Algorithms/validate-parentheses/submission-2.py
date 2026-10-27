class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for c in s:
            if c in pairs.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return bool(len(stack) == 0)