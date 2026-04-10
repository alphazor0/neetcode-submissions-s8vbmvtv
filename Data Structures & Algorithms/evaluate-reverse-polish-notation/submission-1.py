class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(('+', '-', '*', '/'))
        res = 0
        for n in tokens:
            if n not in operators:
                stack.append(int(n))    # ✅ conversion ici
            elif n == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)     # ✅ pas de res séparé
            elif n == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif n == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            elif n == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
        return stack[0]
                

        