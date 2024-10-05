class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new_list = []
        for i in words:
            new_list.extend(i.split(separator))
        last_list = [i for i in new_list if i]
        return last_list