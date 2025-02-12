class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        new = []
        count = 0
        for i in range(len(s) - k + 1):
            new.append(s[i : i + k])
        for i in new:
            if int(i) == 0:
                continue
            if num % int(i) == 0:
                count += 1
        return count
