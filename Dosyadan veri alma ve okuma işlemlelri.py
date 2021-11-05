#Bu derste göreceğimiz fonksiyonlar
#read() Bu fonksiyonda dosyanın içindeki şeylerin hepsini almış olacağız ve print fonksiyonu ile de ekrana yazdırabiliriz
#readline() Dosyanın içindekileri satır satır almak için kullanılır.
#readlines() Bu fonksiyonda dosyanın içindeki bütün satırları gösteriyor ama liste şeklinde gösteriyor.

dosya = open("yazılım.txt","r")

print(dosya.read())
#print(dosya.readline())
#print(dosya.readlines())
