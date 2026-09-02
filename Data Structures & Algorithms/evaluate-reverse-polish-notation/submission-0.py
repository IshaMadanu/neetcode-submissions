class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #iterate thru arry
        # if num, add to stack, if operator, compute with last two nums in stack

        stack = []

        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num2 - num1)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    if num1 != 0:
                        stack.append(int(num2 / num1))
            
        return stack[0]