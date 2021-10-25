dersler ={"Ahmet": ["Veri Tabanları","İşletim Sistemleri"],"Oğuz":["Script Dersi","Nesne Programlama Dersi"], "Mehmet":["Lineer Denklemler"]} 

isim  = input("İsim Giriniz:")

print("() in aldığı dersler:".format(isim))
for i in (dersler[isim]):
    print(i)