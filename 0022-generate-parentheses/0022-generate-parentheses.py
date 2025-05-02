class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Sonuçları saklamak için bir liste oluşturuyoruz
        result = []

        # Geri izleme (backtracking) fonksiyonunu tanımlıyoruz
        def backtrack(current: str, open_count: int, close_count: int):
            # Eğer geçerli bir kombinasyon oluşturduysak (yani 2*n uzunluğunda bir string olduysa)
            if len(current) == 2 * n:
                # Geçerli kombinasyonu sonuca ekliyoruz
                result.append(current)
                return

            # Eğer açılan parantez sayısı 'n' den küçükse, bir açık parantez '(' ekleyebiliriz
            if open_count < n:
                # Yeni bir açık parantez ekliyoruz ve geri izleme fonksiyonunu çağırıyoruz
                backtrack(current + '(', open_count + 1, close_count)

            # Eğer kapanan parantez sayısı açılan parantez sayısından küçükse, bir kapanan parantez ')' ekleyebiliriz
            if close_count < open_count:
                # Yeni bir kapanan parantez ekliyoruz ve geri izleme fonksiyonunu çağırıyoruz
                backtrack(current + ')', open_count, close_count + 1)

        # Başlangıçta boş bir string ile başlıyoruz ve her iki sayıyı (open_count ve close_count) sıfır yapıyoruz
        backtrack("", 0, 0)

        # Sonuçları döndürüyoruz
        return result
        