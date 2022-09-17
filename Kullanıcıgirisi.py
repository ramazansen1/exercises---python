"""KULLANICI GİRİŞİ"""


print(("-"*30) + "\nKULLANICI GİRİŞİ\n" + ("-"*30))

sys_kullanici_adi = "abc123"
sys_parola = "12345"
guvenlik_kodu = "basari"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı adını giriniz: ")
    parola = input("Parolanızı giriniz: ")
    if sys_kullanici_adi != kullanici_adi and sys_parola == parola:
        print("Kullanıcı adınız yanlış.")
        giris_hakki -= 1
    elif sys_kullanici_adi == kullanici_adi and sys_parola != parola:
        print("Parolanız yanlış...")
        giris_hakki -= 1
    elif sys_kullanici_adi != kullanici_adi and sys_parola != parola:
        print("Kullanıcı adınız ve parolanız yanlış...")
        giris_hakki -= 1
    else:
        print("Sisteme hoşgeldiniz...")
        break
    if giris_hakki == 0:
        print("Giriş hakkınız biti...")
        yenileme = input("Kullanıcı adı ve parola yenilemek ister misiniz?\nYenilemek için 'e/E' çıkış yapmak için 'q/Q' basınız.\n")
        if yenileme == "e" or yenileme == "E":
            kod = input("Güvenlik Kodunu giriniz: ")
            if kod == guvenlik_kodu:
                yka = input("Yeni Kullanıcı Adınızı giriniz: ")
                yp = input("Yeni Parolanızı Oluşturunuz: ")

                sys_kullanici_adi = yka
                sys_parola = yp
                print("Kullanıcı Adınız ve Şifreniz Başarı İle Değiştirildi. ")
                continue
            else:
                print("Hesabınız Bloke Edilmiştir. Lütfen desteğe başvurunuz..")
                break
