while True:
    try:
        ilkSayi = int(input("İlk sayiniz: "))
        ikinciSayi = int(input("İkinci sayiniz: "))

        islem = input("Yapmak istediginiz islem türü(+,-,*,/),(Cikmak icin q): ")

        if islem == "q":
            break
        elif islem == "+":
            total = ilkSayi+ikinciSayi
        elif islem == "-":
            print("İsleminiz mutlak degere alinacaktir.")
            total = ilkSayi-ikinciSayi
            total = abs(total)
        elif islem == "*":
            total = ilkSayi*ikinciSayi
        elif islem == "/":
            total = ilkSayi/ikinciSayi
        else:
            print("Hatali islem girdiniz.")
        
        print(f"İslem sonucunuz: {total}")

    except Exception as ex:
        print("Hatali giris yaptiniz.",ex)
            