class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        count_zero = 0
        count_one = 0
        left = 0

        for i in range (len(s)):
            if s[i] == '0':
                count_zero += 1
            else:
                count_one += 1
        
            while (count_zero > k and count_one > k):
                if s[left] == '0':
                    count_zero -= 1
                else:
                    count_one -= 1
                left += 1

            count += (i - left + 1)

        return count

        