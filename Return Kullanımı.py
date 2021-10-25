def kokbul(a,b,c):
    delta = b*b -4*a*c
    if delta <0:
        print("Reel kök bulunamadı..")
        return
    x1 = (-b - delta**0.5)/2*a
    x2 = (-b + delta**0.5)/2*a  

    return (x1,x2)

a =int(input("a:")) 
b =int(input("b:")) 
c =int(input("c:")) 


sonuc = kokbul(a,b,c)

print(sonuc)

#Return dış dünyaya değer göndermek için kullanılır.
#Return fonksiyonları bitirir(5. satırda olduğu gibi..)