import math
import time
"""def faktoriyelal():
    sayi = int(input("Sayı gir:"))
    x = math.factorial(sayi)
    print(("{} sayısın faktoriyeli = {}".format(sayi,math.factorial(sayi))))
faktoriyelal()"""
"""def hipotenüsal():
    kenar1 = int(input("1. Dik Kenarı Giriniz: "))
    kenar2 = int(input("2. Dik Kenarı Giriniz: "))
    x = math.hypot(kenar1,kenar2)
    print("{} ve {} kenarlarının hipotenüsü = {}.".format(kenar1,kenar2,math.hypot(kenar1,kenar2)))
hipotenüsal()"""
"""def faktoriyelal(s):
    return math.factorial(s)
sayi2 = int(input("Sayı Giriniz: "))
print("{} sayısının faktoriyeli = {}".format(sayi2,faktoriyelal(sayi2)))"""
"""def hipotenüsal(a,b):
    return math.hypot(a,b)
kenar1 = int(input("1. Dik Kenarı Giriniz: "))
kenar2 = int(input("2. Dik Kenarı Giriniz: "))
print("{} ve {} kenarlarının hipotenüsü = {}".format(kenar1,kenar2,math.hypot(kenar1,kenar2)))"""
"""def üsbulma(a,b):
    return math.pow(a,b)
sayi1 = int(input("A sayısını giriniz: "))
sayi2 = int(input("B sayısını giriniz: "))
print("{} üssü sonucu = {}".format(sayi1,sayi2,üsbulma(sayi1,sayi2)))"""

"""def logBulma(l):
    return math.log10(l)
sayi3 = int(input("10'luk tabanda sayı giriniz: "))
print("{} onluk tabanda kaşılığı = {}".format(sayi3,logBulma(sayi3)))"""

"""def usAl():
    sayı1 = int(input(" sayının tabanını giriniz : "))
    sayı2 = int(input(" üssü giriniz : "))
    print("işleminiz yapılıyor...")
    time.sleep(1)
    x = math.pow(sayı1, sayı2)
    print("{} üssü {} = {} ".format(sayı1, sayı2, math.pow(sayı1, sayı2)))
usAl()"""


"""def usAl(a,b):
    return math.pow(a,b)
sayı1 = int(input(" sayının tabanını giriniz : "))
sayı2 = int(input(" üssü giriniz : "))
print("{} üssü {} = {} ".format(sayı1, sayı2, usAl(sayı1,sayı2)))"""

m=[[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]

numbers=[i for l in m for e in l for i in e]
print(numbers)

*x,y,z=(4,8,15,16,23,42)
print(x)
print(y)

# enumerate_zip

adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']

for i, e in enumerate(adlar): # burada index olarak olmasına gerek yok start noktası verilebilir.
    print(i, "indexsindeki eleman", e)

"""çıktı:0 indexsindeki eleman Tyler
      1 indexsindeki eleman Blake
      2 indexsindeki eleman Cory
      3 indexsindeki eleman Cameron"""

for i, e in enumerate(adlar, start=1): # başlama değerinden sonra 1 arttırarak devam ediyor.
    print(i, "lokasyonundaki eleman", e)
"""çıktı: 1 lokasyonundaki eleman Tyler
       2 lokasyonundaki eleman Blake
       3 lokasyonundaki eleman Cory
       4 lokasyonundaki eleman Cameron"""

# zip()

ogrenciler = ["ogrenci_1", "ogrenci_2", "ogrenci_3"]
notlar = [90,80,72]

for s,g in zip(ogrenciler,notlar):
    print(s,g)
"""çıktı:
ogrenci_1 90
ogrenci_2 80
ogrenci_3 72
"""

# zip örnek

# Her ayki karı hesaplamak
satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for i in range(len(maliyet)):
    s = satis[i]
    c = maliyet[i]

    kar = s - c
    print(f'Total profit: {kar}')

for s,c in zip(satis,maliyet):
    kar = s-c
    print((f'Total profit: {kar}'))

# zip() ile Dictionary Yaratmak

keys = ['isim', 'soyad', 'ulke', 'is']
values = ['Denis', 'Walker', 'Turkey', 'data scientist']

d = {} # boş dic yaarattık

for k,v in zip(keys,values):
    d[k] = v # dic yeni eleman eklemek
print(d)

d = {} # boş dic yaarattık

for i in range(len(keys)):
    k = keys[i]
    v = values[i]
    d[k] = v
print(d)

x = 7
def f(x):
    res = 5
    res = res * res
    if x % 2 == 0:
        print("Sonuc:", res)
        return res
    else:
        print("Sonuc: ", res)

        return res + 10

f(4) # sonuç : 25 ama patika da sonuç 2525 çıktı :S