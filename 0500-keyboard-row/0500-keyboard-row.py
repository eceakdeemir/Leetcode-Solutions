class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        List1 = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for i in words:
            word = set(i.lower())
            if word.issubset(row1) or word.issubset(row2) or word.issubset(row3):
                List1.append(i)
        return List1 