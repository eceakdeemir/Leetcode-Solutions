class Solution:
    def is_vowel(self, word: List[str]):
        arr = []
        vowel = ['a','e','i','o','u']
        for i in range(0,len(word)):
            if word[i][0] in vowel and word[i][-1] in vowel:
                arr.append(1)
            else:
                arr.append(0)
        return arr

    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        arr = self.is_vowel(words)
        count = 0
        for i in range(left, right + 1):
            if arr[i] == 1:
                count += 1
            else:
                continue
        return count 