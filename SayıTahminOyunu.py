print("-"*50)
print("""
    Sayı Tahmin Oyununa Hoşgeldiniz
    1 - 100 Arasında Bir Sayı Tahmin Ediniz
    Çıkmak için pes / Pes yazınız.
""")
print("-"*50)

import random as rnd

can = 3
rastegeleSayi = rnd.randint(1, 100)

deneme = 0
tahminler = []
while True:
    tahmin = input("Lütfen Tahmin Ettiğiniz Sayıyı Girin: ").lower()

    if tahmin.isdigit():
        tahmin = int(tahmin)

        if tahmin > 100:
            print("Girdiniz değer verilen aralıktan büyüktür.")
            # can -= 1
        elif tahmin < rastegeleSayi:
            # can -= 1
            deneme += 1
            tahminler.append(tahmin)
            print(f"{deneme}. tahmin: {tahmin}\nDaha büyük sayı giriniz.")
        elif tahmin > rastegeleSayi:
            # can -= 1
            deneme += 1
            tahminler.append(tahmin)
            print(f"{deneme}. tahmin: {tahmin}\nDaha küçük bir sayı giriniz.")
        else:
            print(f"Tebrikler, Tuttuğum Sayı: {rastegeleSayi}")
            break
        # if can == 0:
        #     print(f"Üzgünüm canınız bitti...\nTuttuğum sayı: {rastegeleSayi}")
        #     break
    else:
        if tahmin in ["pes", "Pes"]:
            print(f"Pes ettin, Tahminim: {rastegeleSayi}")
            enYakin = tahminler[0]
            for i in tahminler:
                uzaklik = abs(rastegeleSayi - i)
                tahminUzk = abs(rastegeleSayi - enYakin)
                if uzaklik < tahminUzk:
                    enYakin = i
            print(f"En yakın tahmininiz {enYakin}")
            break
            # yakinTahmin = min(tahminler, key=lambda x: abs(x - rastegeleSayi))
            # print(f"Tuttuğum sayiya en yakın tahmininiz: {yakinTahmin}")
            # break
        else:
            print("Hatalı Giriş Yaptınız!")
            continue
