class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x not in ['-', '+', '*', '/']:
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == '*':
                    stack.append(a * b)
                if x == '/':
                    stack.append(int(b/a))
                if x == '+':
                    stack.append(b + a)
                if x == '-':
                    stack.append(b - a)
        
        return stack.pop()
        