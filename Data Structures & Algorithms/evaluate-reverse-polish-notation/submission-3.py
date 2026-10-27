class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                a = int(stack.pop())
                b = int(stack.pop())

                if token == "+":
                    r = b + a
                if token == "-":
                    r = b - a
                if token == "*":
                    r = b * a
                if token == "/":
                    r = b / a
                stack.append(r)
            else:
                stack.append(token)
        
        return int(stack[0])