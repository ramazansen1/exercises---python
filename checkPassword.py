trKarakterler = ["ş", "ç", "ğ", "ü", "ö", "ı", "İ"]
ozelKarakterler = ["!", "#", "@"]


class CheckPassword:
    def __init__(self, password) -> None:
        self.testPassword = password

    def isValidPassword(self):

        try:
            if len(self.testPassword) < 8:
                raise Exception("uygun olmayan parola - minimum karakter politikası")

            for i in self.testPassword:
                if i in trKarakterler:
                    raise Exception("uygun olmayan parola - tr karakter politikasi")

            if not any(i in ozelKarakterler for i in self.testPassword):
                raise Exception("uygun olmayan parola - !, # yada @ içermeli politikası ")

            print("uygun parola")
        except Exception as e:
            print(e, "lütfen tekrar deneyiniz!")


testPassword = input("Lütfen test için parola giriniz: ")
c = CheckPassword(testPassword)
c.isValidPassword()


