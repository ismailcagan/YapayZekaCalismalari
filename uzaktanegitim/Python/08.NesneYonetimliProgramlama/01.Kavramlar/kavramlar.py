# Class
class Kedi:
    pass

# Class Attribute
class Kedi:
    tur = "Ev Kedisi"

# Class Method
class Kedi:
    tur = "Ev Kedisi"
    
    @classmethod
    def KedininTuru(cls):
        print(f"Kedinin Türü :{cls.tur}")

# Constructor
class Kedi:
    tur = "Ev Kedisi"
    def __init__(self):
        self.ad = "Melek"
    
    @classmethod
    def KedininTuru(cls):
        print(f"Kedinin Türü :{cls.tur}")

# Parameterized Constructor
class Kedi:
    tur = "Ev Kedisi"
    def __init__(self,ad):
        self.ad = ad
    
    @classmethod
    def KedininTuru(cls):
        print(f"Kedinin Türü :{cls.tur}")

# Destructor
class Kedi:
    tur = "Ev Kedisi"
    
    def __init__(self,ad):
        self.ad = ad
    def __del__(self):
        print("Nesne Silindi")
        
    def __str__(self):
        return(f"Kedinin Adı :{self.ad}")
    
    @classmethod
    def KedininTuru(cls):
        print(f"Kedinin Türü :{cls.tur}")

# Instance Attribute
class Kedi:
    tur = "Ev Kedisi"
    
    def __init__(self,ad,yas):
        self.ad = ad
        self.yas = yas
        
    def __del__(self):
        print("Nesne Silindi")
        
    def __str__(self):
        return f"Kedinin Adı :{self.ad}\n Kedinin Yasi :{self.yas}"
    
    @classmethod
    def KedininTuru(cls):
        print(f"Kedinin Türü :{cls.tur}")

# Instance Method
class Kedi:
    tur = "Ev Kedisi"
    
    def __init__(self,ad,yas):
        self.ad = ad
        self.yas = yas
        
    def __del__(self):
        print("Nesne Silindi")
        
    def __str__(self):
        return f"Kedinin Adı :{self.ad}\n Kedinin Yasi :{self.yas}"
    
    def Beslen(self):
        return self.ad,"Beslendi"
    
    @classmethod
    def KedininTuru(cls):
        print(f"Kedinin Türü :{cls.tur}")


# Instantiation
kediMelek = Kedi("Melek",5)
kediPamuk = Kedi("Pamuk",3)
print("Melek",kediMelek)
print(kediMelek.Beslen())
print("Pamuk",kediPamuk)