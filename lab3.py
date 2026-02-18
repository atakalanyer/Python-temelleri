try:
    ilkSayi = int(input("İlk sayinizi giriniz: "))
    ikinciSayi = int(input("İkinci sayinizi giriniz: "))

    total = ilkSayi/ikinciSayi
    kalan = ilkSayi%ikinciSayi

    print(f"Kalansiz: {int(total)}, Ondalikli: {total}, Kalan: {kalan}")

except ZeroDivisionError as ex:
    print("Sifira bölüm olamaz.")

finally:
    print("İslem tamamlandi.")