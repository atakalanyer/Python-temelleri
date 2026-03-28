sehirler=set()
for i in range(0,5):
    sehir = input("Şehir adı giriniz: ")
    sehirler.add(sehir)

dsehir = input("Şehir adı giriniz: ")

if dsehir in sehirler:
    print("Bu şehir daha önce girilmiş.")