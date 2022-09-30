# Bankamatik Uygulaması

print("-" * 37)
print("""

BANK ATM MAKİNASINA HOŞ GELDİNİZ

    İŞLEMLER

    1- Şifre Gir
    2- Hesap Bilgileri 
    3- Bakiye Sorgulama
    4- Para Yatırma
    5- Para Çekme
    6- Havale Yapma

    Çıkmak için "q/Q basınız.
""")
print("-" * 37)

hesapA = {
    'ad': 'Ali Veli',
    'hesapNo': '12345678',
    'subeAdi': 'Çarşı Şubesi',
    'IBAN' : 'TRXXXXXXXXX',
    'bakiye': 3000,
    'ekHesap': 2000

}

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda {hesap['ekHesap']} TL bulunmaktadır.")
def havaleYap(hesap):
    bankaKodu = int(input("Lütfen Banka Kodunuzu Giriniz: "))
    havaleBankaKodu = int(input("Lütfen Havale Yapmak İstediğiniz Banka Kodunu Giriniz: "))
    havaleMiktar = int(input("Lütfen Göndermek İstediğiniz Parayı Giriniz: "))
    kesinti = 0
    toplam = hesap['bakiye'] + hesap['ekHesap']

    if bankaKodu != havaleBankaKodu:
        kesinti = havaleMiktar * 0.005
        if hesap['bakiye'] > havaleMiktar:
            hesap['bakiye'] -= havaleMiktar + kesinti
            print(f"Bankamız bu işlem için sizden {kesinti} TL kesinti ücreti alacaktır!")
            print("Paranız başarıyla gönderilmiştir!\nGüncel bakiyeniz;")
            bakiyeSorgula(hesap)
        elif hesap['bakiye'] < havaleMiktar:
            print("Üzgünüz,yetersiz bakiye..")
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h)")
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = havaleMiktar - hesap['bakiye'] - kesinti
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                hesap['bakiye'] = 0
                print(f"Bankamız bu işlem için sizden {kesinti} TL kesinti ücreti alacaktır!")
                print("Paranız başarıyla gönderilmiştir!\nGüncel bakiyeniz;")
                bakiyeSorgula(hesap)
            else:
                print("İşleminiz iptal edilmiştir!")
        elif hesap['bakiye'] == havaleMiktar:
            ekHesapKullanilacakMiktar = havaleMiktar - hesap['bakiye'] - kesinti
            hesap['ekHesap'] += ekHesapKullanilacakMiktar
            hesap['bakiye'] = 0
            print(f"Bankamız bu işlem için sizden {kesinti} TL kesinti ücreti alacaktır!")
            print("Paranız başarıyla gönderilmiştir!\nGüncel bakiyeniz;")
            bakiyeSorgula(hesap)
    else:
        if hesap['bakiye'] >= havaleMiktar:
            hesap['bakiye'] -= havaleMiktar
            print(f"Bankamız bu işlem için sizden {kesinti} TL kesinti ücreti alacaktır!")
            print("Paranız başarıyla gönderilmiştir!\nGüncel bakiyeniz;")
            bakiyeSorgula(hesap)
        else:
            ekHesapKullanilacakMiktar = -havaleMiktar + hesap['bakiye']
            hesap['ekHesap'] += ekHesapKullanilacakMiktar
            hesap['bakiye'] = 0
            print(f"Bankamız bu işlem için sizden {kesinti} TL kesinti ücreti alacaktır!")
            print("Paranız başarıyla gönderilmiştir!\nGüncel bakiyeniz;")
            bakiyeSorgula(hesap)

while True:
    islem = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
    if islem == "q" or islem == "Q":
        print("Sistemden Çıkış yapılıyor.\nLütfen Kartınızı Almayı Unutmayınız!\n")
        break
    elif islem == "6":
        havaleYap(hesapA)

        # elif hesap['bakiye'] >= havaleMiktar:
        #     hesap['bakiye'] -= havaleMiktar
        #     print(f"Bankamız bu işlem için sizden bir ücret almayacaktır!")
        #     print("Paranız gönderilmiştir.\nGüncel bakiyeniz;")
        #     bakiyeSorgula(hesap)
        # else:
        #     print(f"Bankamız bu işlem için sizden bir ücret almayacaktır!")
        #     toplam = hesap['bakiye'] + hesap['ekHesap']
        #
        #     if toplam >= havaleMiktar:
        #         print("Üzgünüz bakiyeniz yetersiz..")
        #         ekHesapKullanimi = input("Ek Hesap Kullanılsın mı? (e/h)")
        #         if ekHesapKullanimi == "e":
        #             ekHesapKullanilacakMiktar = havaleMiktar - hesap['bakiye']
        #             hesap['bakiye'] = 0
        #             hesap['ekHesap'] -= ekHesapKullanilacakMiktar
        #             print("Paranızı alabilirsiniz.")
        #             bakiyeSorgula(hesap)
        #         else:
        #             print("İşleminiz iptal edilmiştir.")
        #     else:
        #         print("Üzgünüz bakiyeniz yetersiz..")
        #         eksiBakiye = input("Eksi bakiyeye düşmek ister misiniz? (e/h)")
        #         if eksiBakiye == "e":
        #             ekHesapKullanilacakMiktar = havaleMiktar - hesap['bakiye']
        #             hesap['bakiye'] = 0
        #             hesap['ekHesap'] -= ekHesapKullanilacakMiktar
        #             print("Paranızı alabilirsiniz.")
        #             bakiyeSorgula(hesap)
        #         else:
        #             print("İşleminiz iptal edilmiştir.")


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

# import random
#
# def sayi_uret(baslangıc=0, bitis=500, adet=6):
#     sayilar = set()
#
#     while len(sayilar) < adet:
#         sayilar.add(random.randrange(baslangıc,bitis))
#     return sayilar
# sayi_uret()




