class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record_list = []
        for i in operations:
            if i == 'D':
                record_list.append(record_list[-1] * 2)
            elif i == 'C':
                record_list.pop()
            elif i == '+':
                record_list.append(record_list[-1] + record_list[-2])
            else:
                record_list.append(int(i))
        toplam = 0
        for i in record_list:
            toplam += i
        return toplam
