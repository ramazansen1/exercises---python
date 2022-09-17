# ATM programı

print("""***************************************\nATM Makinesine Hoşgeldiniz

İşlemler

1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme

Programdan çıkmak için 'q' a basın.
***************************************
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz: ")
    if işlem == "q":
        print("Yine bekleriz.")
        break
    elif işlem == "1":
        print("Bakiyeniz {}'dir.".format(bakiye))
    elif işlem == "2":
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar
    elif işlem == "3":
        miktar = int(input("Miktarı giriniz: "))
        if (bakiye - miktar) < 0:
            print("Yetersiz Bakiye....")
            continue
        bakiye -= miktar
        print("Kalan bakiye {}'dir.".format(bakiye))

    else:
        print("Geçersiz işlem....")

















