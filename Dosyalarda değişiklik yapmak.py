"""with open("yazılım.txt","a") as dosya:
    dosya.write("Php: Rasmus Lerdorf")"""
#Yukarıdaki kod satırı otomatik olarak dosyanın sonuna yazmamızı sağlıyor.
# "r+" modu dosyaya hem okuma hem de yazma izni veriyor.

"""with open("yazılım.txt","r+") as dosya:
    data = dosya.read()
    dosya.seek(0)
    data = "Php: Rasmus Lerdorf\n" + data
    dosya.write(data) """
#Yukarıdaki kod satırı ile de dosyanın en başına istediğimizi yazdırabiliyoruz.

with open("yazılım.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"Php: Rasmus Lerdorf")
    dosya.seek(0)
    dosya.writelines(data)