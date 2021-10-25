boy = float(input("Boyunuzu giriniz(m):"))
kilo = int(input("Kilonuzu giriniz(kg):"))

vki = kilo/(boy*boy)

def vucutkitleindeksi():
    if(vki < 18):
        print("Zayıfsınız...")
    elif(vki >= 18 and vki < 25):
        print("İdeal kilodasınız...")
    elif(vki >= 25 and vki <30 ):
        print("Hafif Kilolusunuz.Kilo vermeniz gerekiyor...")
    elif(vki >= 30):
        print("Obezsiniz.Acilen kilo vermeniz gerekiyor...")
    

vucutkitleindeksi()