class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Farklı şeker türlerini set içinde saklayarak sayısını buluyoruz
        candies = set(candyType)
        
        # Alice'in yiyebileceği şeker türlerinin sayısı, ya farklı türlerin sayısı ya da n/2 ile sınırlıdır
        return min(len(candies), len(candyType) // 2)


            