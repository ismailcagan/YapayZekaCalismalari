import numpy as np
import pandas as pd

# BURADA YAPAY VERİLER OLUŞTURULDU

np.random.seed(42)

set1no = 900
set2no = 100

df1 = pd.DataFrame(
    {
        "feature_1": np.random.normal(loc=0, scale=1, size=set1no),
        "feature_2": np.random.normal(loc=0, scale=1, size=set1no),
        "target": [0] * set1no,
    }
)

df2 = pd.DataFrame(
    {
        "feature_1": np.random.normal(loc=0, scale=1, size=set2no),
        "feature_2": np.random.normal(loc=0, scale=1, size=set2no),
        "target": [1] * set2no,
    }
)

print(df1.head())
"""
   feature_1  feature_2  target
0   0.496714   0.368673       0
1  -0.138264  -0.393339       0
2   0.647689   0.028745       0
3   1.523030   1.278452       0
4  -0.234153   0.191099       0
"""

print(df2.head())
"""
   feature_1  feature_2  target
0   1.901191   0.696954       1
1  -0.060661  -0.333819       1
2  -0.708407   1.173125       1
3  -1.513714   0.369642       1
4  -1.803140  -0.107302       1
"""
# YAPAY VERİLER BİRLEŞTİRİLDİ

df = pd.concat([df1, df2]).reset_index(drop=True)  # iki veriyi birleştirdik
print(df)
"""
     feature_1  feature_2  target
0     0.496714   0.368673       0
1    -0.138264  -0.393339       0
2     0.647689   0.028745       0
3     1.523030   1.278452       0
4    -0.234153   0.191099       0
..         ...        ...     ...
995  -0.370011   1.070150       1
996  -0.258796  -0.026521       1
997   1.598647  -0.881875       1
998   0.560919  -0.163067       1
999  -0.295480  -0.744903       1
"""

# BİRLEŞTİRİLEN VERİLER HAKINDA BİLGİLER EDİNİLDİ

print(df["target"].unique()) # [0 1]

print(df["target"].value_counts())
"""
target
0    900
1    100
Name: count, dtype: int64
"""
# Yukarıdaki bilgilere göre 900 tane 0 100 tane 1 değerivar bu dengesiz 
#    veri setine örnek. BU durumda ne yapılır onu inceleyeceğiz


# 1- upsampling (upsample minority) --> Az verileri çoğaltma(Kopyala Yapıştır Yapar)

# 2- downsampling (downsample majority) --> çoğunluğu azaltmak (Veriyi Siler)


# 1-) upsampling (upsample minority) --> Az verileri çoğaltma

df_minority = df[df["target"] == 1] # sadece 1 olanları getirdik
print(df_minority)

"""
     feature_1  feature_2  target
900   1.901191   0.696954       1
901  -0.060661  -0.333819       1
902  -0.708407   1.173125       1
903  -1.513714   0.369642       1
904  -1.803140  -0.107302       1
..         ...        ...     ...
995  -0.370011   1.070150       1
996  -0.258796  -0.026521       1
997   1.598647  -0.881875       1
998   0.560919  -0.163067       1
999  -0.295480  -0.744903       1
"""

df_majority = df[df["target"] == 0]
print(df_majority)
"""
     feature_1  feature_2  target
900   1.901191   0.696954       1
901  -0.060661  -0.333819       1
902  -0.708407   1.173125       1
903  -1.513714   0.369642       1
904  -1.803140  -0.107302       1
..         ...        ...     ...
995  -0.370011   1.070150       1
996  -0.258796  -0.026521       1
997   1.598647  -0.881875       1
998   0.560919  -0.163067       1
999  -0.295480  -0.744903       1
"""

from sklearn.utils import resample

df_minority_upsampled = resample(df_minority,replace=True,n_samples=len(df_majority),random_state=42)

print(df_minority_upsampled.shape) # (900, 3)

print(df_minority_upsampled)
"""
     feature_1  feature_2  target
951   1.775311   1.261922       1
992  -0.436386   1.188913       1
914  -0.268531  -1.801058       1
971  -0.214921  -2.940389       1
960  -0.134309  -0.054894       1
..         ...        ...     ...
952  -1.193637  -0.905732       1
965  -1.662492   0.089581       1
976  -0.562168   1.124113       1
942  -0.548725   0.269127       1
974   1.310309  -0.018709       1

[900 rows x 3 columns]
"""

df_upsample = pd.concat([df_majority,df_minority_upsampled])
print(df_upsample)
"""
     feature_1  feature_2  target
0     0.496714   0.368673       0
1    -0.138264  -0.393339       0
2     0.647689   0.028745       0
3     1.523030   1.278452       0
4    -0.234153   0.191099       0
..         ...        ...     ...
952  -1.193637  -0.905732       1
965  -1.662492   0.089581       1
976  -0.562168   1.124113       1
942  -0.548725   0.269127       1
974   1.310309  -0.018709       1

[1800 rows x 3 columns]
"""

print(df_upsample["target"].value_counts())
"""
target
0    900
1    900
Name: count, dtype: int64
"""

# 2-) downsampling (downsample majority) --> çoğunluğu azaltmak 

df_majority_downsampled = resample(df_majority,replace=True,n_samples=len(df_minority),random_state=42)
print(df_majority_downsampled)
"""
     feature_1  feature_2  target
102  -0.342715   0.059630       0
435   0.074095  -0.337086       0
860   0.202923   1.639965       0
270   1.441273   0.758929       0
106   1.886186   0.895193       0
..         ...        ...     ...
201   0.560785  -2.896255       0
269   0.130741   0.853416       0
862   1.547505   0.075434       0
815  -1.485560  -0.090533       0
270   1.441273   0.758929       0

[100 rows x 3 columns]
"""

print(df_majority_downsampled["target"].value_counts())
"""
target
0    100
Name: count, dtype: int64
"""

df_downsapled = pd.concat([df_majority_downsampled,df_minority])
print(df_downsapled)
"""
target
0    100
Name: count, dtype: int64
"""

print(df_downsapled["target"].value_counts())
"""
target
0    100
1    100
Name: count, dtype: int64
"""

# SMOTE (Synthetic Minority Over-Sampling) --> Benzer Veriler Oluşturur

print(df)
"""
     feature_1  feature_2  target
0     0.496714   0.368673       0
1    -0.138264  -0.393339       0
2     0.647689   0.028745       0
3     1.523030   1.278452       0
4    -0.234153   0.191099       0
..         ...        ...     ...
995  -0.370011   1.070150       1
996  -0.258796  -0.026521       1
997   1.598647  -0.881875       1
998   0.560919  -0.163067       1
999  -0.295480  -0.744903       1

[1000 rows x 3 columns]
"""
print(df["target"].value_counts())
"""
target
0    900
1    100
Name: count, dtype: int64
"""

import matplotlib.pyplot as plt
plt.scatter(df["feature_1"],df["feature_2"],c=df["target"])


from imblearn.over_sampling import SMOTE

oversample = SMOTE()
(x,y) = oversample.fit_resample(df[["feature_1","feature_2"]],df["target"])

print(x)
"""
      feature_1  feature_2
0      0.496714   0.368673
1     -0.138264  -0.393339
2      0.647689   0.028745
3      1.523030   1.278452
4     -0.234153   0.191099
...         ...        ...
1795   0.701868  -0.173309
1796   1.545917  -1.335943
1797   1.358114  -0.225781
1798   0.486916  -0.147628
1799   0.504733  -1.114370

[1800 rows x 2 columns]
"""

print(y)
"""
0       0
1       0
2       0
3       0
4       0
       ..
1795    1
1796    1
1797    1
1798    1
1799    1
Name: target, Length: 1800, dtype: int64
"""

oversample_df = pd.concat([x,y],axis=1)
print(oversample_df)
"""
      feature_1  feature_2  target
0      0.496714   0.368673       0
1     -0.138264  -0.393339       0
2      0.647689   0.028745       0
3      1.523030   1.278452       0
4     -0.234153   0.191099       0
...         ...        ...     ...
1795   0.701868  -0.173309       1
1796   1.545917  -1.335943       1
1797   1.358114  -0.225781       1
1798   0.486916  -0.147628       1
1799   0.504733  -1.114370       1

[1800 rows x 3 columns]
"""

print(oversample_df["target"].value_counts())

"""
target
0    900
1    900
Name: count, dtype: int64
"""

plt.scatter(oversample_df["feature_1"],oversample_df["feature_2"], c = oversample_df["target"])


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









