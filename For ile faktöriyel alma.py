faktöriyel = 1

while True:
    sayı = int(input("pozitif bir sayı giriniz:"))
    if sayı <= 0:
        print("Lütfen negatif olmayan bir sayı giriniz.")
    else:
        for i in range(1,sayı+1):
            faktöriyel *=i 
        print("Faktöriyel:", faktöriyel)
        break