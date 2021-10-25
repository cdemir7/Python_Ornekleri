try:
    dosya = open("yazılımbilimi.txt","r")

except IOError:
    print("Dosya Bulunamadı..."),

finally:
    dosya.close()