class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        def getNums():
            num2 = stack.pop()
            num1 = stack.pop()
            return num1, num2

        for token in tokens:
            if token == "+":
                num1, num2 = getNums()
                stack.append(num1 + num2)

            elif token == "-":
                num1, num2 = getNums()
                stack.append(num1 - num2)

            elif token == "/":
                num1, num2 = getNums()
                stack.append(int(float(num1) / num2))

            elif token == "*":
                num1, num2 = getNums()
                stack.append(num1 * num2)

            else:
                stack.append(int(token))
    
        return stack[0]

