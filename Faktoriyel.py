### Faktöriyel Bulma

print("""******************************

Faktoriyel Bulma Programı

Çıkmak için q'ya basın
******************************""")

while True:
    sayi = input("Sayı: ")
    if sayi == "q":
        print("Program Sondandırılıyor...")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            print("Faktoriyel",faktoriyel,"i:",i)
            """Çıktı: Faktoriyel 1 i: 2
                      Faktoriyel 2 i: 3
                      Faktoriyel 6 i: 4
                      Faktoriyel 24 i: 5
                      Faktoriyel 120"""
            faktoriyel *= i
        print("Faktoriyel",faktoriyel)















