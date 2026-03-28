import re

while True:

    password=input("Parolanizi giriniz:")

    def check_password(psw):
        if re.search("[ç,ğ,i,ö,ş,ü]",password):
            raise Exception("Türkce karakter kullanamazsiniz.")
        else:
            print("Parola olusturuldu.")

    try:
        check_password(password)
    except Exception as ex:
        print(ex)
    else:
        break