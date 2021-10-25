sayi = int(input("Bir sayı giriniz:"))

def negatifmipozitifmi():
    if(sayi > 0):
        print("Girdiğiniz sayı pzoitiftir.")
    elif(sayi <0):
        print("Girdiğiniz sayı negatiftir.")
    elif(sayi == 0):
        print("Girdiğiniz sayı negatif veya pozitif değildir.")

negatifmipozitifmi()