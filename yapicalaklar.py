def ekleme(liste,todo):
    liste.append(todo)

def silme(liste,cikar):
    if cikar<1 or cikar>len(liste):
        print("Gecersiz numara")
        return
    liste.pop(cikar-1)

liste = []
while True:
    print("===== TO DO LİST =====")
    islem=int(input("1-Ekleme\n2-Cikarma\n3-Listele\n0-Cikis"))

    if islem not in range(0,4):
        print("Lütfen gecerli bir islem numarasi giriniz. ") 
        continue

    if islem == 1:
        to_do=input("Yapilacak isi giriniz: ")
        ekleme(liste,to_do)

    elif islem == 2:
        silmeNum=int(input("Silinecek is numarasi: "))
        silme(liste,silmeNum)

    elif islem == 3:
        for i, item in enumerate(liste, start=1):
            print(i, "-", item)

    elif islem == 0:
        print("Cikis yapiliyor.")
        break

    x=10
    y=20
    print(x+y)