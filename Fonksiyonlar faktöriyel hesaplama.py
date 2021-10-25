def factoriyel(numara):
    faktöriyel = 1
    for i in range(1,numara+1):
        faktöriyel *= i
    print("Faktöriyel:",faktöriyel)




sayı = int(input("Bir sayı giriniz:"))

factoriyel(sayı)
