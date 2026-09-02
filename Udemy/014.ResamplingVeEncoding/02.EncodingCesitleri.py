
# ENCODİNG ÇEŞİTLERİ

"""
Encoding (Kodlama), yapay zeka ve bilgisayar bilimlerinde en basit tanımıyla: 
İnsanların anladığı verileri, bilgisayarların ve yapay zeka modellerinin 
işleyebileceği sayısal (matematiksel) formata dönüştürme işlemidir.
Neden Encoding Yaparız?Yapay Zeka Matematikle Çalışır: 
Yapay zeka modelleri (algoritmalar) aslında devasa matematik formülleridir.
"Kırmızı", "Kadın", "İstanbul" gibi kelimelerle toplama, çıkarma veya çarpma yapamazlar.
Format Zorunluluğu: Bilgisayarların bu verileri işleyebilmesi için kelimelerin 
mutlaka 0, 1, 2.5 veya vektörler (sayı dizileri) gibi numerik değerlere çevrilmesi gerekir.
Günlük Hayattan Bir ÖrnekBir anket yaptığınızı ve bilgisayara veri girdiğinizi düşünün:
Ham Veri (İnsan için): "Evet", "Hayır", "Belki"
Encoded Veri (Bilgisayar için): Evet = 1, Hayır = 0, Belki = 2
"""

# 1-) One - Hot Encoding
"""
Detaylı Mantık: Kategoriler arasında hiyerarşi yoksa (Nominal veri) kullanılır. 
Her benzersiz kategori için yeni bir sütun (özellik) yaratılır. 
İlgili kategorinin olduğu satıra 1, diğerlerine 0 verilir.

Dezavantajı: Kategori sayısı çoksa (Örn: 81 il), 81 yeni sütun oluşur ve 
veri seti aşırı şişer (Boyutluluk Laneti).

Örnek Tablo:
Elimizde "Ev Tipi" adında bir sütun olsun:

Satır          Ev Tipi (Ham Veri)
1              Daire
2              Villa
3              Müstakil
4              Daire


One-Hot Encoding Sonrası:
Satır     Ev_Tipi_Daire       Ev_Tipi_Villa       Ev_Tipi_Müstakil
1         1                   0                   0
2         0                   1                   0
3         0                   0                   1
4         1                   0                   0

"""

# 2-) Label Encoding
"""
Detaylı Mantık: Genellikle Hedef Değişken (Target/Y) 
yani tahmin etmek istediğimiz sütun metinsel olduğunda tercih edilir. 
Kategorileri alfabe sırasına veya gelişigüzel sırayla 0'dan başlayarak numaralandırır.
Kritik Uyarı: Giriş özelliklerinde (X) kullanılırsa, 
yapay zeka 2 değerini 0 değerinden daha üstün/büyük zannedebilir. 
Bu yüzden giriş verilerinde sıralama yoksa kullanılmamalıdır.

Örnek Tablo:
Bir müşterinin ürünü "Satın Alma Durumu" (Hedef Değişken):

Satır     Satın Alma (Ham Veri)
1         İptal Edildi
2         Satın Aldı
3         İade Etti
4         Satın Aldı

Label Encoding Sonrası: (Alfabetik sıraya göre: İade=0, İptal=1, Satın Aldı=2)

Satır     Satın Alma (Encoded)
1         1
2         2
3         0
4         2
"""

# 3-) Ordinal Encoding
"""
Detaylı Mantık: Kategoriler arasında doğal bir sıra veya hiyerarşi varsa (Ordinal veri) kullanılır. 
Label Encoding'e çok benzer ama buradaki fark, sayısal değerleri bizim belirlediğimiz 
hiyerarşiye göre elle atamamızdır.

Örnek Tablo:
Kullanıcılardan gelen "Baharat Derecesi" geri bildirimleri:

Satır     Baharat Derecesi (Ham Veri)
1         Orta
2         Acı
3         Az
4         Acı

Hiyerarşiyi modele şöyle öğretiriz: Az = 0, Orata = 1, Acı = 2.

Ordinal Encoding Sonrası:
Satır     Baharat Derecesi (Encoded)
1         1
2         2
3         0
4         2
"""

# 4-) Frequency Encoding

"""
Detaylı Mantık: Kategorilerin veri setinde görünme sıklığını (frekansını) veya oranını değer olarak atar. 
Özellikle kategori sayısı çok fazla olduğunda (Örn: Posta kodları, markalar) sütun sayısını artırmadan 
veriyi sayısallaştırmak için harika bir yöntemdir.

Örnek Tablo:
Elimizde 10 satırlık bir veri seti olsun ve "Telefon Markası" sütununda 5 adet Apple, 3 adet Samsung, 2 adet Xiaomi bulunsun.

Satır     Telefon (Ham Veri)
1         Apple
2         Samsung
3         Xiaomi
4         AppleFrequency 
Encoding Sonrası: (İster adet, ister oran yazılır. Genelde oran/yüzde tercih edilir: Apple = 5/10 = 0.5)

Satır          Telefon (Encoded)        Açıklama
1              0.5                      Toplam verinin %50'si Apple
2              0.3                      Toplam verinin %30'u Samsung
3              0.2                      Toplam verinin %20'si Xiaomi
4              0.5                      Apple

"""


# 5-) Target Encoding(Mean Encoding)

"""
Detaylı Mantık: Kategorik sütundaki her bir değerin, tahmin edilmek istenen hedef sütundaki 
(Target) ortalaması alınarak kodlanmasıdır. 
Modelin hedef değişkenle olan korelasyonunu doğrudan yakaladığı için yarışmalarda 
(Kaggle gibi) çok sık kullanılır.Risk: Overfitting (Aşırı Öğrenme) riski çok yüksektir. 
Model veriyi ezberleyebilir.

Örnek Tablo:
Amacımız: "Şehir" verisine bakarak "Ev Fiyatı" tahmini yapmak olsun.

Satır     Şehir (Giriş)       Ev Fiyatı (Hedef / Target)
1         İstanbul            4.000.000 TL
2         Ankara              2.000.000 TL
3         İstanbul            6.000.000 TL
4         Ankara              3.000.000 TL
Hesaplama:İstanbul için ortalama fiyat: (4M + 6M) / 2 = 5.000.000Ankara için ortalama fiyat: (2M + 3M) / 2 = 2.500.000

Target Encoding Sonrası: (Şehir sütunu ortalama fiyatlarla değişir)

Satır     Şehir (Encoded)     Ev Fiyatı (Target)
1         5.000.000           4.000.000 TL
2         2.500.000           2.000.000 TL
3         5.000.000           6.000.000 TL
4         2.500.000           3.000.000 TL

"""


# 6-) Binary ENcoding

"""
Detaylı Mantık: One-Hot Encoding'in yarattığı "çok fazla sütun" problemini çözmek için matematiksel bir hile kullanır. 
Önce kategorilere sayı verilir (Label Encoding), sonra o sayılar ikilik tabana (0 ve 1'lere) çevrilir ve her basamak bir sütun olur.
Örnek Senaryo:Elimizde 8 farklı meslek olsun. One-Hot yapsak 8 sütun açılır. 
Binary Encoding bunu nasıl çözer?
"Mühendis" kategorisine 5 sayısı atansın.5 sayısının ikilik tabandaki karşılığı 101'dir.
8 kategoriyi temsil etmek için sadece 3 sütun (özellik) yeterlidir (\(2^3=8\)).

Örnek Tablo:
Satır     Meslek (Ham Veri)        Sayısal Karşılığı      İkilik (Binary) Karşılığı
1         Mühendis                 5                      101
2         Doktor                   2                      010

Binary Encoding Sonrası:
Satır               Meslek_B1          Meslek_B2            Meslek_B31 
1 (Mühendis)        1                  0                    1
2 (Doktor)          0                  1                    0

Gördüğünüz gibi 8 farklı meslek için 8 sütun yerine sadece 3 sütunla işi çözmüş olduk.

"""

"""
pythonimport pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder
import category_encoders as ce

# ---------------------------------------------------------
# SİMÜLASYON VERİ SETİ OLUŞTURMA
# ---------------------------------------------------------
# Tüm senaryoları tek seferde görmek için yapay bir veri seti kuralım
data = {
    'Ev_Tipi': ['Daire', 'Villa', 'Müstakil', 'Daire'],          # One-Hot için (Nominal)
    'Baharat': ['Orta', 'Acı', 'Az', 'Acı'],                    # Ordinal için (Sıralı)
    'Sehir': ['Ankara', 'İstanbul', 'Ankara', 'Ankara'],         # Frequency için (Çok tekrarlı)
    'Meslek': ['Mühendis', 'Doktor', 'Mühendis', 'Doktor'],     # Binary için
    'Ev_Fiyati':,                      # Target için (Sürekli Hedef Değişken)
    'Satin_Alma': ['Iptal', 'Satin_Aldi', 'Iade', 'Satin_Aldi'] # Label için (Kategorik Hedef Değişken)
}

df = pd.DataFrame(data)
print("--- HAM VERİ SETİ ---")
print(df, "\n" + "="*50 + "\n")

# ---------------------------------------------------------
# 1-) ONE-HOT ENCODING (Pandas get_dummies ile en pratik yol)
# ---------------------------------------------------------
# Ev_Tipi sütununu her kategori için yeni bir sütuna böler
df_one_hot = pd.get_dummies(df, columns=['Ev_Tipi'], dtype=int)
print("1-) ONE-HOT ENCODING SONUCU:")
print(df_one_hot[['Ev_Tipi_Daire', 'Ev_Tipi_Müstakil', 'Ev_Tipi_Villa']], "\n")


# ---------------------------------------------------------
# 2-) LABEL ENCODING (Scikit-Learn)
# ---------------------------------------------------------
# Satin_Alma hedef sütununu alfabetik sıraya göre 0, 1, 2 yapar
le = LabelEncoder()
df['Satin_Alma_Encoded'] = le.fit_transform(df['Satin_Alma'])
print("2-) LABEL ENCODING SONUCU:")
print(df[['Satin_Alma', 'Satin_Alma_Encoded']], "\n")


# ---------------------------------------------------------
# 3-) ORDINAL ENCODING (Scikit-Learn)
# ---------------------------------------------------------
# Baharat derecelerini kendi belirlediğimiz hiyerarşik sıraya koyarız
siralar = [['Az', 'Orta', 'Acı']] # 0=Az, 1=Orta, 2=Acı
oe = OrdinalEncoder(categories=siralar)
df['Baharat_Encoded'] = oe.fit_transform(df[['Baharat']])
print("3-) ORDINAL ENCODING SONUCU:")
print(df[['Baharat', 'Baharat_Encoded']], "\n")


# ---------------------------------------------------------
# 4-) FREQUENCY ENCODING (Pandas)
# ---------------------------------------------------------
# Şehirlerin veri setindeki yüzdelik oranlarını hesaplar ve yerine yazar
sehir_oranlari = df['Sehir'].value_counts(normalize=True)
df['Sehir_Encoded'] = df['Sehir'].map(sehir_oranlari)
print("4-) FREQUENCY ENCODING SONUCU:")
print(df[['Sehir', 'Sehir_Encoded']], "\n")


# ---------------------------------------------------------
# 5-) TARGET ENCODING (Category Encoders)
# ---------------------------------------------------------
# Şehir sütununu, Ev_Fiyati (Target) ortalamasına göre kodlar
te = ce.TargetEncoder(cols=['Sehir'])
# Not: Gerçek projelerde Overfitting'i önlemek için sadece Train setine fit edilir!
df_target = te.fit_transform(df['Sehir'], df['Ev_Fiyati'])
print("5-) TARGET ENCODING SONUCU (Ev Fiyatı Ortalamasına Göre Şehir):")
print(pd.concat([df['Sehir'], df_target], axis=1), "\n")


# ---------------------------------------------------------
# 6-) BINARY ENCODING (Category Encoders)
# ---------------------------------------------------------
# Meslek sütununu ikilik tabana çevirerek az sayıda sütun oluşturur
be = ce.BinaryEncoder(cols=['Meslek'])
df_binary = be.fit_transform(df['Meslek'])
print("6-) BINARY ENCODING SONUCU:")
print(df_binary)


Kod Çıktı Mantığı ve İpuçlarıpd.get_dummies: Projelerde hızlıca One-Hot Encoding yapmak için 
Scikit-Learn kütüphanesinden çok daha pratiktir.map(): Frequency encoding yaparken ekstra bir 
kütüphaneye ihtiyaç duymadan Pandas'ın kendi fonksiyonuyla frekansları eşleştirmemizi sağlar.
category_encoders: Target ve Binary encoding gibi ileri düzey yöntemleri tek satırda çözmek için 
veri biliminde standart olarak kullanılan harika bir kütüphanedir.
"""









