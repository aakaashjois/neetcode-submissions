class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        opening = set(["(", "{", "["])
        closing = set([")", "}", "]"])
        
        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            
            if c in closing:
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
        
        return bool(len(stack) == 0)