def faktoriyel(sayi):
    if sayi < 0:
        raise Exception("Sayi negatif olamaz.")
    total = 1
    for x in range(1, sayi + 1):
        total *= x
    return total


while True:
    giris = input("Sayi gir (cikis için q): ")

    if giris.lower() == "q":
        print("Programdan cikiliyor ")
        break

    try:
        sayi = int(giris)
        print(f"{sayi} faktoriyeli: {faktoriyel(sayi)}")
    except ValueError:
        print("Geçerli bir sayi gir.")
    except Exception as ex:
        print(ex)