# Veri tabanı,aynı bir excel tablosu gibi tablo ve sütunları ilerde kullanabilmemiz için saklanan alana denir.
#SQLite veritabanı yani database'si internetsiz çalışabilen bir databasedir.
# SQL bir sorgu dilidir. Veri tabanı üzerinde çalıştırabilecek komutları ve sorguları çalıştıran bir dildir.
import sqlite3
con = sqlite3.connect("pythondersleri.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT, numara INT, ogrencinotu INT)")

def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Gökçe','DEMIR',321,93)")
    con.commit()
    con.close()

tabloolustur()
degerekle()