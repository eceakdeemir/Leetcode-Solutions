class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        count = 0

        for i in s:
            if count == 0 and i == '(':
                count += 1
            elif i == '(':
                count += 1
                stack.append(i)
            elif count == 1 and i == ')':
                count -= 1
            else:
                count -= 1
                stack.append(i)
        return "".join(stack)