from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Uzunluk kontrolü
        if len(s1) > len(s2):
            return False

        # 2. Karakter sayımlarını hesapla
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        # 3. İlk pencereyi kontrol et
        if s1_count == window_count:
            return True
        
        # 4. Pencereyi kaydır
        for i in range(len(s1), len(s2)):
            # Yeni karakter ekle
            window_count[s2[i]] += 1
            # Eski karakteri çıkar
            window_count[s2[i - len(s1)]] -= 1
            
            # Eğer eski karakterin sayısı sıfıra düştüyse onu kaldır
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
                
            # 5. Güncellenen pencereyi kontrol et
            if window_count == s1_count:
                return True
        
        # 6. Eşleşme bulunamazsa
        return False
