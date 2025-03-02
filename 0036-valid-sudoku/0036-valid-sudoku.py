class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stack = []
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if (number != '.'):
                    stack += [(i, number), (number, j), (i // 3, j // 3, number)]
        return len(stack) == len(set(stack))