class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        count = {}
        start = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1

            while count[s[end]] > 2:
                count[s[start]] -= 1
                #if count[s[start]] == 0:
                    #del count[s[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

        kaaabcdefg

        """Python'daki .get() metodu, bir sözlükte (dictionary) belirli bir anahtarın değerini almanızı sağlar. Eğer anahtar sözlükte mevcut değilse, bu durumda bir hata vermek yerine varsayılan bir değer döndürür. Bu, hata ayıklama işlemini kolaylaştırır.

Kullanımı:
value = my_dict.get(key, default_value)
key: Aramak istediğiniz anahtar.
default_value: Anahtar mevcut değilse döndürülecek değer (bu parametre isteğe bağlıdır; belirtilmezse None döner)."""