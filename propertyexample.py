class Device:

    def __init__(self, dType, ip, port, username, password):

        self.dType = dType
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    @property
    def dType(self):
        return self._dType

    @dType.setter
    def dType(self, value):
        self._dType = value

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def __str__(self):
        return f"cihaz tipi {self.dType} olan {self.ip} IP adresli cihaz {self.port}. portu dinliyor." \
               f"Kullanıcı adı {self.username} parola {self.password}"

dType = input("Cihaz Tipini Giriniz: ")
ip = input("Ip Bilgisini Giriniz: ")
port = input("Port Bilgisini Giriniz: ")
username = input("Kullanıcı Adını Giriniz: ")
password = input("Parola Bilgisini Giriniz: ")

dev = Device(dType, ip, port, username, password)
print(dev)
