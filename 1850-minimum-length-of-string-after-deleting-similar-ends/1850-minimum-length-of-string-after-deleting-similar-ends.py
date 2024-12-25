class Solution:
    def minimumLength(self, s: str) -> int:
        first = 0
        last = len(s) - 1
        while first < last and s[first] == s[last]:
            x = s[first]
            while first <= last and s[first] == x:
                first += 1
            while first <= last and s[last] == x:
                last -= 1
        return last - first + 1
