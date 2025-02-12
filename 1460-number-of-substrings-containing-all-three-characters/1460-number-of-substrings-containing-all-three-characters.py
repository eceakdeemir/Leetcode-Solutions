from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0
        count = 0
        freq = Counter()

        for right in range(n):
            # Şu anki karakteri pencereye ekle
            freq[s[right]] += 1
            
            # Eğer pencere en az bir 'a', bir 'b' ve bir 'c' içeriyorsa
            while len(freq) == 3:
                # Geçerli alt dizilerden her biri, left ile right arasındaki bir başlangıç noktasından başlar ve right'tan sonrasına kadar olan tüm alt dizilerdir
                count += (n - right)
                
                # Pencereyi daralt
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
        
        return count
