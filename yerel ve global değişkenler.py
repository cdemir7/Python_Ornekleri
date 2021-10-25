#Yerel Ve Global Değişkenler
#Fonsiyonların içinde tanımladığımız değişkenler yerel dışındakiler global fonksiyondur.


a = 10
def fonksiyon():
    global a
    a = 5
    print(a)

fonksiyon()
print(a)