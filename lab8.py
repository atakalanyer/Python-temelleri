ilkUrun = float(input("İlk urunun fiyatini ondalikli sekilde giriniz: "))
ikinciUrun = float(input("İkinci urunun fiyatini ondalikli sekilde giriniz: "))

total = ilkUrun+ikinciUrun

kdv= total * (18/100)

total+=kdv

print(f"KDV eklendikten sonra genel toplam fiyat: {total}")