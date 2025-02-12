class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        new_list = []

        while (i < len(blocks)):
            x = blocks[i: i + k]
            if (len(x) == k):
                new_list.append(x.count('W'))
            i += 1
        return min(new_list)