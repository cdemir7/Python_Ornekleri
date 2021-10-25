#dosya açarken bizim 3 tane modumuz var. ilki 'write' modu. bu mod eğer aynı isimde başka dosya yoksa dosyayı oluşturuyor ve içine bir şeyler yazmamızı sağlıyor.
#eğer aynı isimde başka dosya o dosyayı silip aynı isimde yani dosya açıyor ve içine yazma izni veriyor.
#ikinci modumuz 'read' modu. Bu modda olan dosyayı açıp okumamızı sağlıyor.
#üçüncü modda 'append' modu. bu da var olan dosyanın içindeki b,ilgileri değiştirmemizi sağlıyor.
#ancak eğer ismi belirtilen dosya yoksa dosyayı oluşturuyor ve içine bir şeyler yazmamızı sağlıyor.
#eğer başka bir dizinde dosya oluşturmak istersek yolunu belirtmemiz gerekir.
#dosya = open("C:/Users/user/Desktop/Yazılım.txt","w")  


#dosya = open("Yazılım.txt","w") 
dosya = open("Yazılım.txt","a") 
dosya.write("iyimisin")
