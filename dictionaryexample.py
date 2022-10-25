araba = {
    "Marka": {
    "Seri": {},
    "Model": {},
    "Yıl": {},
    "Yakıt:": {},
    "Vites": {}
}
}

arabalar = []
cikis = ""
while cikis != "0":
    araba = {"Marka": input("Araba Markası Ekle, Çıkmak İçin [0]: "), "Seri": input("Seri Bilgisi Giriniz: "),
             "Model": input("Model Bilgisini Giriniz: "), "Yil": int(input("Yıl Bilgisini Giriniz: ")),
             "Yakit": input("Yakıt Bilgisini Giriniz: "), "Vites": input("Vites Bilgisini Giriniz: ")}
    arabalar.append(araba)
    cikis = input("Daha Fazla Araba Eklemek İstiyor Musunuz? (1/0): ")
print(f"Galeride ki Araba Listemiz;\n {arabalar}")