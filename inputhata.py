while True:
    deger=input("Bir sayi giriniz:")
    if deger=="q":
        break
    try:
        result=int(deger)
    except:
        print("Sayi girmediniz.")
    