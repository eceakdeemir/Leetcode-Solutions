class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        len_list = len(code)
        new_list = [0] * len_list
        if k == 0:
            return new_list
    

        for i in range(len_list):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                   new_list[i] += code[j % len_list]
            elif k < 0: 
                for j in range(i - 1, i - 1 + k, -1):
                   new_list[i] += code[j % len_list]
        return new_list
