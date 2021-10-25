import urllib.request

url1 = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.gezginfoto.com.tr%2Fimages%2Fmakaleler%2Fetkili_manzara_11.jpg&imgrefurl=https%3A%2F%2Fwww.gezginfoto.com.tr%2Fmakale%2F271-etkili-manzara-foto%25C4%259Fraflar%25C4%25B1-%25C3%25A7ekmek.html&tbnid=ta_Ie0bSF8gtzM&vet=12ahUKEwiGoKPI_ZPsAhVF_4UKHQkSBxAQMygAegUIARChAQ..i&docid=qnZHCtfhL8EUXM&w=425&h=635&q=manzara%20foto%C4%9Fraf%C4%B1&safe=strict&ved=2ahUKEwiGoKPI_ZPsAhVF_4UKHQkSBxAQMygAegUIARChAQ"
url2 = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fd.neoldu.com%2Fnews%2F5893.jpg&imgrefurl=https%3A%2F%2Fwww.neoldu.com%2Fmanzara-fotografi-cekmenin-puf-noktalari-2846h.htm&tbnid=sdeO6s7rHn_uqM&vet=12ahUKEwiGoKPI_ZPsAhVF_4UKHQkSBxAQMygCegUIARClAQ..i&docid=vSoqROM8Vj4jbM&w=660&h=320&q=manzara%20foto%C4%9Fraf%C4%B1&safe=strict&ved=2ahUKEwiGoKPI_ZPsAhVF_4UKHQkSBxAQMygCegUIARClAQ"
url3 = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.superprof.com.tr%2Fblog%2Fwp-content%2Fuploads%2F2020%2F02%2Fmanzara-fotografi-nasil-cekilir.jpg&imgrefurl=https%3A%2F%2Fwww.superprof.com.tr%2Fblog%2Fmanzara-fotografi-nasil-cekilir%2F&tbnid=Qn38IPp14BClOM&vet=12ahUKEwiGoKPI_ZPsAhVF_4UKHQkSBxAQMygDegUIARCnAQ..i&docid=qOK30PjMdMiSNM&w=1050&h=701&q=manzara%20foto%C4%9Fraf%C4%B1&safe=strict&ved=2ahUKEwiGoKPI_ZPsAhVF_4UKHQkSBxAQMygDegUIARCnAQ"

urllistesi = [url1,url2,url3]
say = 1
for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim" + str(say)+".jpg")
    say +=1
