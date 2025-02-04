class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for count in s:
            if stack and stack[-1] == count:
                stack.pop()
            else:
                stack.append(count)
        return ''.join(stack)