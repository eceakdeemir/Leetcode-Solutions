class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = set(candyType)
        if len(candies) > len(candyType) / 2:
            return int(len(candyType) / 2)
        else:
            return int(len(candies))

            