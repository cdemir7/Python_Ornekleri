#Kullanıcı ismi ve Parola Kontrolü Programı

kullanıcı_ismi = input("Kullanıcı ismini giriniz:")
parola = input("Parolayı giriniz:")

if kullanıcı_ismi == "cihan" and parola == "demir":
    print("Programa Hoşgeldiniz...")

elif kullanıcı_ismi != "cihan" and parola == "demir":
    print("Kullanıcı ismini yanlış girdiniz...")

elif kullanıcı_ismi == "cihan" and parola != "demir":
    print("Parolanızı yanlış girdiniz...")

else:
    print("Hatalı Kullanıcı adı ve Parola....")

