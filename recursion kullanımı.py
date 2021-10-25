#RECURSİON

# 1-) FONKSİYONUN KENDİSİNİN SONSUZA KADAR ÇALIŞTIRMAMASI İÇİN BİTİŞ DURUMU YARATMAK GEREKLİDİR.
# 2-) FONKSİYONUN BELLİ ŞARTLARDA KENDİNİ ÇAĞIRMASI GEREKLİ

#For döngüsü ile yazımı
"""def topla(liste):
    toplam = 0

    for i in liste:
        toplam += i
    return toplam

print(topla([1,2,3,4]))"""

#recursiyon fonksiyonu ile yazımı 
def topla(liste):
    if(len(liste)) == 0:
        return 0
    else:
        return liste[0] + (topla(liste[1:]))

print(topla([1,2,3,4]))