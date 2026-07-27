class DosyaTool:
    def __init__(self,adres="defter.csv",**kwargs):
        self.adres = adres
        self.alanlar = ["Adi","Soyadi","Telefon"]
        for key, value in kwargs.items():
            if key == "alanlar":
                self.alanlar = value
        self.DosyaAc()
        self.Liste = self.dosya.readlines()
    
    def DosyaAc(self):
        import os
        if os.path.exists(self.adres):
            self.dosya = open(self.adres,"r+",encoding="UTF-8")
        else:
            self.dosya = open(self.adres,"w+",encoding="UTF-8")

    def Listeleme(self):
        for i in range(len(self.Liste)):
            kayit = ""
            for item in self.Liste[i].split(";"):
                kayit += item +" "
            satir = f"{i+1}-{kayit}"
            print(satir,end="")

    def GirisYap(self):
        kayit = ""
        for item in self.alanlar:
            kayit += input(f"{item} Giriniz :") +";"
        kayit = kayit.rsplit(";") +"\n"
        return kayit
    
    def KayitListeleme(self):
        self.Listeleme()
    
    def KayitEkleme(self):
        self.Liste.append(self.GirisYap())
        
    def KayitDüzelt(self):
        self.Listeleme()
        kayitNum = int(input("Güncellemek istediğiniz numarayı giriniz :"))
        self.Liste[kayitNum-1] = self.GirisYap()
        
    def KayitSil(self):
        self.Listeleme()
        kayitNum = int(input("Güncellemek istediğiniz numarayı giriniz :"))
        del self.Liste[kayitNum-1]
    
    def Menu(self):
        Menu = """
            1-)Listele
            2-)Ekleme
            3-)Güncelleme
            4-)Silme
            5-)Çıkış
            İşlem Seçiniz
        """
        anahtar = 1
        while anahtar == 1:
            islem = input(Menu)
            if islem == "5":
                anahtar = 0
            elif islem == "1":
                self.KayitListeleme()
            elif islem == "2":
                self.KayitEkleme()
            elif islem == "3":
                self.KayitDüzelt()
            elif islem == "4":
                self.KayitSil()
        else:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(self.liste)
            self.dosya.flush()
            
    def __del__(self):
        self.dosya.close()

class BankaDefter(DosyaTool):
    def __init__(self):
        super().__init__(adres="hesap.csv", alanlar=["Banka Hesap No","Tip","Tutar"])
        self.Menu()

class TelefonDefter(DosyaTool):
    def __init__(self):
        super().__init__(adres="defter.csv", alanlar=["Adi","Soyadi","Telefon"])
        self.Menu()

banka = BankaDefter()

        
