class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        first = 0
        last = len(s) - 1
        s = list(s)
        while first < last:
            if not s[first].isalpha():
                first += 1
                continue
            if not s[last].isalpha():
                last -= 1
                continue
            if s[first].isalpha() and s[last].isalpha():
                s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1
        return ("".join(s))