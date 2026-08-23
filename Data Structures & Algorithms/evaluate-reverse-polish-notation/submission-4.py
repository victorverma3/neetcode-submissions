class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                second = stack.pop()
                first = stack.pop()
                res = first + second
                stack.append(res)
            elif t == "-":
                second = stack.pop()
                first = stack.pop()
                res = first - second
                stack.append(res)
            elif t == "*":
                second = stack.pop()
                first = stack.pop()
                res = first * second
                stack.append(res)
            elif t == "/":
                second = stack.pop()
                first = stack.pop()
                res = int(float(first) / second)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack.pop()