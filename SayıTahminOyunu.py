# Sayı Tahmin Oyunu

print("""**********************************************
Sayı Tahmin Oyununa Hoşgeldiniz!

1 ile 50 arasında ki sayıyı tahmin ediniz...
Eğer oyundan çıkmaz isterseniz 'pes/Pes' yazınız...
**********************************************
""")

import random
import time

rastgele_sayi = random.randint(1,50)
tahmin_hakkı = 7

while True:
    tahmin = input("Tahmininiz nedir? ")

    if tahmin.isdigit(): # girilen değer sayılardan mı oluşuyor harflerden mi ?
        tahmin = int(tahmin)
        if tahmin > 50:
            print("Sayı karşılaştırılıyor...")
            time.sleep(1)
            print("Girdiğiniz sayı verilen aralığın dışında!")
            print("1-50 aralığında bir tahmin giriniz!")
            tahmin_hakkı -=1
        elif tahmin < rastgele_sayi:
            tahmin = int(tahmin)
            print("Sayı karşılaştırılıyor...")
            time.sleep(1)
            print("Daha yüksek sayı giriniz...")
            tahmin_hakkı -=1
        elif tahmin > rastgele_sayi:
            print("Sayı Karşılaştırılıyor...")
            time.sleep(1),
            print("Daha düşük sayı giriniz...")
            tahmin_hakkı -=1
        else:
            print("Sayı Karşılaştırılıyor...")
            time.sleep(1)
            print("Tebrikler! Sayımız: ",rastgele_sayi)
            break
        if tahmin_hakkı == 0:
            print("Üzgünüm Tahmin Hakkınız Bitti...")
            break
    else:
        if tahmin == "pes" or tahmin == "Pes":
            print("Pes Ettin! Tahminim", rastgele_sayi)
            break
        else:
            print("Hatalı giriş yaptınız.")
            continue


