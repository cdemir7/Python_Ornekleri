#Kullanıcı adı ve Parola Kontrolü (While ile)

defkullanıcı_adı = "cihan"
defparola = "demir"

while True:
    kullanıcı = input("Kullanıcı adınızı giriniz:")
    parola = input("Parolanızı giriniz:")

    if kullanıcı == defkullanıcı_adı and parola == defparola:
        print("Programa hoşgeldiniz...")
        break

    elif kullanıcı != defkullanıcı_adı and parola == defparola:
        print("Hatalı kullanıcı adı")
        break

    elif kullanıcı == defkullanıcı_adı and parola != defparola:
        print("Hatalı parola")
        print("Şifrenizi değiştirmek ister misiniz? (E/H)")
        cevap = input()
        if cevap == "E" or "e":
            yeniparola = input("Yeni parolanızı giriniz:")
            print("Lütfen bekleyiniz....")
            defparola = yeniparola
            print("Şifre başarıyla değiştirildi...")
        else:
            break    
        
    else:
        print("Tekrar deneyin...")    


    
