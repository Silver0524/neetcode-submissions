class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                stack.append(stack.pop(-2) + stack.pop())
            elif val == "*":
                stack.append(stack.pop(-2) * stack.pop())
            elif val == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif val == "/":
                stack.append(int(stack.pop(-2) / stack.pop()))
            else:
                stack.append(int(val))
        return stack[0]