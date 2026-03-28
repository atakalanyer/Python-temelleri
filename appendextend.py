"""renkler = ["kırmızı", "sarı", "yeşil"]
yeni_renkler = ["pembe", "mor"]

renkler.append(yeni_renkler)
print(renkler)  # Çıktı: ['kırmızı', 'sarı', 'yeşil', ['pembe', 'mor']]

renkler1 = ["kırmızı", "sarı", "yeşil"]
renkler1.extend(yeni_renkler)
print(renkler1)  # Çıktı: ['kırmızı', 'sarı', 'yeşil', 'pembe', 'mor']"""

"""renkler = ["kırmızı", "sarı", "yeşil"]
print(renkler)  # Çıktı: ['kırmızı', 'sarı', 'yeşil']
print(renkler[::-1]) # Çıktı: ['yeşil', 'sarı', 'kırmızı']"""

a = [1, 2]
B=a
B.append(3)
print(a) # Çıktı: [1, 2, 3]

c = a.copy()
c.append(4)
print(a) # Çıktı: [1, 2, 3]
print(c) # Çıktı: [1, 2, 3, 4]