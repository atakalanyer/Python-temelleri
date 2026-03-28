sehirler=[]
for i in range(0,3):
    sehir = input("Şehir adı giriniz: ")
    sehirler.append(sehir)


sehirler = tuple(sehirler)

for sehir in sehirler:
    if sehir.startswith("A"):
        print(sehir)