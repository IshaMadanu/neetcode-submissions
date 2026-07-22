class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top == "(" and char != ")":
                        return False
                    if top == "{" and char != "}":
                        return False
                    if top == "[" and char != "]":
                        return False
        if len(stack) == 0:
            return True
        return False
