# Gelişmiş Bankamatik Uygulaması

print("-" * 37)
print("""

ATM MAKİNASINA HOŞ GELDİNİZ

    İŞLEMLER

    1- Hesap Bilgileri 
    2- Bakiye Sorgulama
    3- Para Yatırma
    4- Para Çekme
    5- Havale Yapma
    6- Kredi Çekme
    7- İletişim

    Çıkmak için "q/Q basınız.
""")
print("-" * 37)

hesapA = {
    'ad': 'Ali',
    'hesapNo': '12345678',
    'subeAdi': 'Çarşı Şubesi',
    'IBAN': 'TRXXXXXXXXX',
    'bakiye': 3000,
    'ekHesap': 2000,
    'krediLimit': 100000,
    'ekHesapLimit': 2000
}

def hesapBilgileri(hesap):
    print(f"Hesap Bilgileriniz;\nAd Soyad: {hesap['ad']}\nHesap No: {hesap['hesapNo']}\nŞube Adı: {hesap['subeAdi']}\nIBAN\t: {hesap['IBAN']}")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda {hesap['ekHesap']} TL bulunmaktadır.")

def paraYatir(hesap):
    yatiralacakMiktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
    if hesap['ekHesap'] < 2000:
        yatiralacakMiktar += hesap['ekHesap'] - hesap['ekHesapLimit']
        hesap['ekHesap'] -= hesap['ekHesap'] - hesap['ekHesapLimit']
        hesap['bakiye'] += yatiralacakMiktar
        print(f"Paranız {hesap['hesapNo']} nolu hesabınıza başarılı bir şekilde yatırılmıştır.")
        bakiyeSorgula(hesap)
    else:
        print("Paranız yatırılıyor. Lütfen bekleyiniz..")
        hesap['bakiye'] += yatiralacakMiktar
        print("Paranız başarılı bir şekilde yatırılmıştır.\nGüncel bakiyeniz;")
        bakiyeSorgula(hesap)

def paraCek(hesap):

    cekilecekMiktar = int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
    if hesap['bakiye'] >= cekilecekMiktar:
        hesap['bakiye'] -= cekilecekMiktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam <= cekilecekMiktar:
            ekHesapKullanimi = input("Ek Hesap Kullanılsın mı? (e/h)")

            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = cekilecekMiktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)

def havaleYap(hesap):
    bankaKodu = int(input("Lütfen Banka Kodunuzu Giriniz: "))
    havaleBankaKodu = int(input("Lütfen Havale Yapmak İstediğiniz Banka Kodunu Giriniz: "))
    havaleMiktar = int(input("Lütfen Göndermek İstediğiniz Parayı Giriniz: "))
    kesinti = 0

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
                ekHesapKullanilacakMiktar = havaleMiktar - hesap['bakiye'] + kesinti
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

def krediCek(hesap):
    krediMiktar = int(input("Çekmek istediğiniz kredi miktarını girin: "))
    if hesap['krediLimit'] < krediMiktar:
        print("Üzgünüz talep ettiğiniz tutarı karşılıyamıyoruz.")
        print("Hesabınıza ait limit 100000 TL'dir.")
        limit = input("Kullanılsın mı? (e/h)")
        if limit == "e":
            kalanMiktar = hesap['krediLimit'] + hesap['ekHesap'] - hesap['ekHesapLimit']
            hesap['ekHesap'] -= hesap['ekHesap'] - hesap['ekHesapLimit']
            hesap['bakiye'] += kalanMiktar
            print(f"Krediniz {hesap['hesapNo']} nolu hesabınıza başarılı bir şekilde aktarılmıştır.")
            print("Güncel bakiyeniz;")
            bakiyeSorgula(hesap)
        else:
            print("İşleminiz iptal edilmiştir.\nTekrar bekleriz.")
    else:
        if hesap['ekHesap'] < 2000:
            kalanMiktar = krediMiktar + hesap['ekHesap'] - hesap['ekHesapLimit']
            hesap['ekHesap'] -= hesap['ekHesap'] - hesap['ekHesapLimit']
            hesap['bakiye'] += kalanMiktar
            print(f"Krediniz {hesap['hesapNo']} nolu hesabınıza başarılı bir şekilde aktarılmıştır.")
            bakiyeSorgula(hesap)
        else:
            hesap['bakiye'] += krediMiktar
            print(f"Krediniz {hesap['hesapNo']} nolu hesabınıza başarılı bir şekilde aktarılmıştır.")
            print("Güncel bakiyeniz;")
            bakiyeSorgula(hesap)

print(f"Hoşgeldiniz,\nMerhaba {hesapA['ad']},")
while True:
    islem = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
    if islem == "q" or islem == "Q":
        print("Sistemden Çıkış yapılıyor.\nLütfen Kartınızı Almayı Unutmayınız!\n")
        break
    elif not 1 <= int(islem) <= 7:
        print("Yanlış bir işlem seçtiniz!")
    elif islem == "1":
        hesapBilgileri(hesapA)
    elif islem == "2":
        bakiyeSorgula(hesapA)
    elif islem == "3":
        paraYatir(hesapA)
    elif islem == "4":
        paraCek(hesapA)
    elif islem == "5":
        havaleYap(hesapA)
    elif islem == "6":
        krediCek(hesapA)
    else:
        print("Bankamız ile 0850xxxx nolu numaradan iletişime geçebilirsiniz!\nİyi günler dileriz.")