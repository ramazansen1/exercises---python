print("-"*37)
print("""
THEBANK ATM MAKİNASINA HOŞ GELDİNİZ

İŞLEMLER

1- Hesap Bilgileri 
2- Bakiye Sorgulama
3- Para Yatırma
4- Para Çekme

Çıkmak için "q/Q basınız.
""")
print("-"*37)

import time
bakiye = 1000
sys_parola = "1234"
# giris_hakkı = 3
# şifre girdisi sor
# kartı kaptır
while True:
    islem = input("Yapmak İsteğiniz İşlemi Seçiniz:\n")
    if islem == "q" or islem == "Q":
        print("Sistemden Çıkış Yapılıyor...\nLütfen Kartınızı Almayı Unutmayın...\nTekrar Bekleriz...")
        break
    elif islem == "1":
        print("Hesap Bilgileri Aktarılıyor...")
        time.sleep(1)
        print("Hesap Bilgileriniz Aşağıdaki gibidir...")
        hesap_bilgileri = "Hesap Sahibi: Ramazan Şen\nHesap no: 123456\nŞube Adı: Çarşı Şubesi\nIBAN: TR***********"
        print(hesap_bilgileri)
    elif islem == "2":
        print("{} TL bakiyeniz vardır.".format(bakiye))
    elif islem == "3":
        yatiralacak_para = int(input("Yatırmak İstediğiniz Tutarı Girin: "))
        bakiye += yatiralacak_para
        print("Hesap bakiyeniz {} TL'dir.".format(bakiye))
    elif islem == "4":
        cekilmek_istenen_para = int(input("Çekmek İstediğiniz Tutarı Girin: "))
        bakiye -= cekilmek_istenen_para
        print("Kalan bakiye {} TL'dir.".format(bakiye))
        if cekilmek_istenen_para > bakiye:
            print("Bakiyeniz yetersizdir...")
            continue
    else:
        print("Geçersiz işlem...")



