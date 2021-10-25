#Eğer bir uygulama yazarken aşağıdaki kalıbı kullanarak dosya yazarsanız kapatmayı unuttuğunuzda python sizin için dosyayı kaptır ve bilgisayarınızı zorlamaz.
with open("yazılım.txt","r") as dosya:
    dosya.seek(10)
    print(dosya.read())
#Yukarıda da seek() donksiyonuna verdiğimiz argümandan sonraki kısmını ekrana yazdırır.

with open("yazılım.txt","r") as dosya:
    dosya.seek(10)
    print(dosya.read())
    dosya.seek(5)
    print(dosya.read)
#Yukarıdaki gibi  bir program yazarsak seek() fonksiyonu normalde 10 karakter ileri atmıştı ama bu diğer işlemde en başa döner ve toplam olarak 15 olmaz 5 karakter ileri gider.

with open("yazılım.txt","r") as dosya:
    dosya.seek(10)
    print(dosya.read(5))
#Yukarıdaki programı çalıştırırsakta 10 katrakter sonrasındaki 5 karakteri ekrana bastıracaktır.

with open("yazılım.txt","r") as dosya:
    dosya.seek(10)
    str1 = dosya.read(5)
    dosya.seek(15)
    str2 = dosya.read(5)
    print(str1,str2)
#Yukarıdaki pRogramı da çalıştırırsak eğer ilk olarak baştan 10 karakter gidip sonraki 5 karakteri bastıracak ve sonrada baştan 15 karakter gidip sonraki 5 karakteri bastıracak.

