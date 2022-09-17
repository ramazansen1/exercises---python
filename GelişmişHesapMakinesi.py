import math
import time
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def karekkokAlma(k):
    return math.sqrt(k)

def faktoriyelal(s):
    return math.factorial(s)

def hipotenusal(a,b):
    return math.hypot(a,b)

def usbulma(a,b):
    return math.pow(a,b)

def logBulma(l):
    return math.log10(l)

def derecedenRadyana(r):
    return math.radians(r)

def radyandanDereceye(d):
    return math.degrees(d)

def sinBulma(s):
    return math.sin(s)

def cosBulma(c):
    return math.cos(c)

def tanjant(t):
    return math.tan(t)

def cotanjant(c):
    return math.cos(c)/math.sin(c)


print("**********************************************\n"
"GELİŞMİŞ HESAP MAKİNESİ PROGRAMI \n"
"LÜTFEN İŞLEM SEÇİN\n"
"1. İşlem = Toplama \n"
"2. İşlem = Çıkarma \n"
"3. İşlem = Çarpma \n"
"4. İşlem = Bölme \n"
"5. İşlem = Karekok Alma \n"
"6. İşlem = Faktoriyel \n"
"7. İşlem = Hipotenüs \n"
"8. İşlem = Sayının Üssünü Bulma \n"
"9. İşlem = Sayının Logaritmasını Bulma \n"
"10. İşlem = Dereceyi Radyana Çevirme \n"
"11. İşlem = Radyanı Dereceye Çevirme \n"
"12. İşlem = Sinüs Hesaplama \n"
"13. İşlem = Cos Hesaplama \n"
"14. İşlem = Tanjant Hesaplama \n"
"15. İşlem = Cotanjant Hesaplama \n"
"16. İşlem = Küp Alan Hesaplama \n"
"17. İşlem = Daire Çevre Hesaplama \n"
"18. İşlem = Daire Alan Hesaplama \n"
"Çıkmak için q/Q basın.\n"
"**********************************************\n")
#sin cos tan cot bunlarda radyan cisnsinden buluyor.



while True:
    islem = input("Yapmak İstediğiniz İşlemi Belirtiniz: ")
    if islem == "q" or islem == "Q":
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(2)
        print("Hesap Makinesi Kapatıldı...")
        break
    elif islem == "1":
        a = float(input("Sayı giriniz: "))
        b = float(input("Sayı giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} + {} = {}".format(a,b,toplama(a,b)))
    elif islem == "2":
        a = float(input("Sayı giriniz: "))
        b = float(input("Sayı giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} - {} = {}".format(a,b,cikarma(a,b)))
    elif islem == "3":
        a = float(input("Sayı giriniz: "))
        b = float(input("Sayı giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} * {} = {}".format(a,b,carpma(a,b)))
    elif islem == "4":
        a = float(input("Sayı giriniz: "))
        b = float(input("Sayı giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} / {} = {}".format(a,b,bolme(a,b)))
    elif islem == "5":
        sayi1 = float(input("Karekök Alınacak Sayıyı Giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} sayısının karesi = {}".format(sayi1, karekkokAlma(sayi1)))
    elif islem == "6":
        sayi2 = int(input("Sayı Giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} sayısının faktoriyeli = {}".format(sayi2, faktoriyelal(sayi2)))
    elif islem == "7":
        kenar1 = int(input("1. Dik Kenarı Giriniz: "))
        kenar2 = int(input("2. Dik Kenarı Giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} ve {} kenarlarının hipotenüsü = {}".format(kenar1, kenar2, math.hypot(kenar1, kenar2)))
    elif islem == "8":
        taban = int(input("Taban sayısını giriniz: "))
        us = int(input("Üs sayısını giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} üssü {} sonucu = {}".format(taban, us, usbulma(taban, us)))
    elif islem == "9":
        sayi3 = int(input("10'luk tabanda sayı giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} onluk tabanda kaşılığı = {}".format(sayi3, logBulma(sayi3)))
    elif islem == "10":
        radyan = int(input("Radyan giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} radyanının derecesi = {}".format(radyan, derecedenRadyana(radyan)))
    elif islem == "11":
        derece = int(input("Dereceyi giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("{} derecesinin radyanı = {}".format(derece, radyandanDereceye(derece)))
    elif islem == "12":
        derece1 = int(input("Derece giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("sin {} = {}".format(derece1, sinBulma(derece1)))
    elif islem == "13":
        derece2 = int(input("Derece giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("cos {} = {}".format(derece2, cosBulma(derece2)))
    elif islem == "14":
        derece3 = int(input("Derece giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("tan {} = {}".format(derece3, tanjant(derece3)))
    elif islem == "15":
        derece4 = int(input("Derece giriniz: "))
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(1)
        print("cot {} = {}".format(derece4, cotanjant(derece4)))
    else:
        print("Hatalı bir işlem seçtiniz.")
        continue





