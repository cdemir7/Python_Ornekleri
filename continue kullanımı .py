listeler = [2,3,4]

for i in range(1,10):
    if i in listeler:
        continue
    print(i)

"""Burada sonuç '1,5,6,7,8,9' olacaktır. 
Çünkü continue deyimi işlemi başa döndürür. 
Bunun için listelerin içindeki sayıları ekrana yazdırmaz""" 