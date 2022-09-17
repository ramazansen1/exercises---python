# def isim_ne():
#     isim = input("İsminiz nedir?:")
#     print(isim)
#
# print(f"Merhaba {isim_ne()}.Nasılsın?")

#
# def isim_ne():
#     isim = input("İsminiz nedir?:")
#     return isim
# print(f"Merhaba {isim_ne()}.Nasılsın?")

import random

def sayi_uret(baslangıc=0, bitis=500, adet=6):
    sayilar = set()

    while len(sayilar) < adet:
        sayilar.add(random.randrange(baslangıc,bitis))
    return sayilar
sayi_uret()




