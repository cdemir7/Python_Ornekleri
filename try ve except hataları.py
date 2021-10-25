sayı1 = input("Sayı1:")
sayı2 = input("Sayı2 :")

try:
    sayı1 = int(sayı1)
    sayı2 = int(sayı2)
    print(sayı1/sayı2)

#except ValueError:
#    print("Lütfen 10'luk tabanlı bir sayı giriniz...")

#except ZeroDivisionError:
#   print("Lütfen Sayı ikiye 0 değerini atamayınız...\n Çünkü Herhangi bir sayı 0'a bölünemez...")

except (ValueError, ZeroDivisionError):
    print("Bir hata oluştu...")