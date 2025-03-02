class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: x[0])
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        arr = []
        for query in queries:
            left, right = 0, len(max_beauty) - 1
            beauty = 0
            while left <= right:
                middle = (left + right) // 2
                if max_beauty[middle][0] <= query:
                    beauty = max_beauty[middle][1]
                    left = middle + 1
                else:
                    right = middle - 1
            arr.append(beauty)
        return (arr)
