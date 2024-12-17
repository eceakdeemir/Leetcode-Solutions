class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 'first' sözlüğü: Her bir sayının ilk göründüğü indeksi tutar
        first = {}
        # 'last' sözlüğü: Her bir sayının son göründüğü indeksi tutar
        last = {}
        # 'count' sözlüğü: Her bir sayının toplam sayısını tutar
        count = {}
        # En büyük dereceyi (en fazla tekrar sayısı) tutmak için değişken
        degree = 0
        
        # Listeyi tek tek geziyoruz
        for i, x in enumerate(nums):
            # Eğer sayıyı daha önce görmediysek, 'first' sözlüğüne kaydediyoruz
            if not x in count:
                first[x] = i
                count[x] = 0
            # Her sayının son görülme indeksini 'last' sözlüğüne kaydediyoruz
            last[x] = i
            # Sayının tekrar sayısını artırıyoruz
            count[x] += 1
            # En yüksek tekrar sayısını güncelliyoruz
            degree = max(degree, count[x]) 
        
        # En küçük alt dizenin uzunluğunu başta sonsuz yapıyoruz
        lensub = float('inf')
        
        # 'count' sözlüğündeki her bir öğe için
        for x in count:
            # Eğer sayının tekrar sayısı, en yüksek dereceye eşitse
            if count[x] == degree:
                # 'first' ve 'last' sözlüklerindeki indeks farkını alıp, uzunluğu hesaplıyoruz
                # +1 ekliyoruz çünkü indeksler sıfırdan başlıyor, ancak uzunluk birden başlar
                lensub = min(abs(first[x] - last[x]) + 1, lensub)
        
        # En küçük alt dizenin uzunluğunu döndürüyoruz
        return lensub
