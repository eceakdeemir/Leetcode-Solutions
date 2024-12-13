class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = {}
        for i in candyType:
            if i in candies:
                candies[i] += 1
            else:
                candies[i] = 1
        candiesLen = len(candies)
        if candiesLen > len(candyType) / 2:
            return int(len(candyType) / 2)
        else:
            return int(candiesLen)

            