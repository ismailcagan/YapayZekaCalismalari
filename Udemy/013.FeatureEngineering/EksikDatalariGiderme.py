"""
1-)Types of Missing Values (EKSİK DEĞER TÜRLERİ)

A-) Missing Completely at Random (MCAR)

    Türkçesiyle Tamamen Rastlantısal Kayıp, veri biliminde veri setindeki eksik (boş)
    değerlerin oluşma şeklini açıklayan en ideal senaryodur.Bir verinin MCAR olması,
    verinin eksik olmasının veri setindeki ne o sütunla ne de başka bir sütunla hiçbir
    alakasının olmaması demektir. Yani veri tamamen şans eseri, rastgele kaybolmuştur.

    Hava Durumu Sensörü Örneği: Bir şehirdeki hava sıcaklığını ölçen bir cihazınız var.
    Cihaz her gün veri kaydediyor. Ancak bir gün yoldan geçen bir kuş gelip cihaza çarpıyor,
    cihaz 2 dakikalığına kapanıyor ve o günün sıcaklık verisi kaydedilemiyor. İşte bu veri MCAR'dır.
    Çünkü o verinin kaybolmasının havanın çok sıcak olmasıyla (kendi değeriyle) veya nem oranıyla
    (başka bir değerle) hiçbir bağı yoktur; tamamen şans eseridir.

B-) Missing at Random (MAR)

    Bir verinin MAR olması, verinin eksik olmasının (boş kalmasının) verinin kendi değeriyle değil,
    veri setindeki başka bir "gözlemlenebilir/bilinen" sütunla ilişkili olması demektir.
    İsmi ilk başta kafa karıştırıcı gelebilir ("Rastlantısal" deniyor ama aslında bir kurala bağlı).
    Buradaki "Rastlantısal" kelimesinin asıl anlamı şudur: Belirli bir grup veya alt küme
    kendi içinde rastgeledir, ancak o grubun eksik veri üretme oranı diğer gruplardan daha yüksektir.

    Sağlık ve Yaş Örneği: Bir hastanede insanların kilo verilerini topluyorsunuz.
    Yaşlı hastaların kilolarının genç hastalara göre çok daha fazla boş bırakıldığını fark ettiniz.
    Yaşlı hastalar tartılmaktan çekindiği için değil, doktorlar yaşlıları yormamak veya ayağa
    kaldırmamak için kilolarını sisteme girmemiş olabilir. Burada kilonun boş kalması şans eseri değildir;
    doğrudan hastanın Yaş sütunundaki değerine bağlıdır.

    Anket ve Cinsiyet Örneği: Bir ankette insanlara "Depresyonda mısınız?" diye soruyorsunuz.
    Erkeklerin bu soruyu kadınlara kıyasla çok daha fazla boş bıraktığını görüyorsunuz.
    Sorunun boş kalma olasılığı, kişinin Cinsiyet sütununa bağlıdır.


C-) Missing Not at Random (MNAR)

    Bir verinin MNAR olması; verinin eksik olmasının (boş kalmasının) doğrudan o verinin kendi gizli değeriyle
    (yani ölçülemediği için bilmediğimiz o değerle) ilişkili olması demektir.
    Yani veri şans eseri veya başka bir sütun yüzünden değil,
    bilerek veya yapısı gereği gizlenmiştir ya da oluşamamıştır.

    Maaş Anketi Örneği (En Klasik Örnek): Bir şirkette çalışanlara maaşlarını soruyorsunuz.
    Çok yüksek maaş alan (örneğin müdürler, CEO'lar) veya asgari ücretin altında çok düşük
    maaş alan çalışanlar gelirlerini ankette boş bırakıyor.
    Burada maaş verisinin boş kalma nedeni, doğrudan maaşın kendisidir.
    Veri, "çok yüksek" veya "çok düşük" olduğu için kayıptır.

    Hava Durumu Sensörü Örneği: Bir dondurucu soğuk bölgesine hava durumu sensörü kurdunuz.
    Ancak hava sıcaklığı -30 derecenin altına düştüğünde sensörün pilleri donuyor ve çalışmıyor.
    Dolayısıyla o günlerin sıcaklık verisi sisteme girilemiyor. Verinin eksik olma nedeni
    doğrudan havanın aşırı soğuk olmasıdır (sıcaklık değerinin kendisidir).

    Üç Eksik Veri Türünün Büyük Özeti (Farkı Anlama)Konuyu tam oturtmak için bir öğrenci
    sınavı üzerinden üçünü kıyaslayalım:
    MCAR (Tamamen Rastlantısal): Öğrenci sınav kağıdını teslim ederken yolda öğretmen bir sayfayı düşürüp kaybediyor.
    (Tamamen şans eseri).

    MAR (Rastlantısal): Sınav süresi yetmediği için arka sayfadaki sorular boş kalıyor.
    (Eksiklik, soru çözme hızına/süreye bağlıdır).

    MNAR (Rastlantısal Olmayan): Öğrenci sorunun cevabını bilmediği için soruyu boş bırakıyor.
    (Eksiklik doğrudan sorunun cevabının (verinin kendisinin) öğrenci tarafından bilinmemesiyle ilgilidir).

2-) Handling Missing Values in Feature Engineering

A-) Removing Missing Values(If Missing is Low)

    Removing Missing Values (If Missing is Low), Türkçesiyle "Eksik Değerleri Silme (Eğer Eksik Veri Oranı Düşükse)",
    veri temizleme sürecinde uygulanan en pratik ve kestirme yöntemdir.Eğer veri setinizdeki eksik (boş) verilerin oranı
    toplam veriye kıyasla çok küçükse (genellikle %5 veya daha azı ise) ve bu verilerin rastgele (MCAR) kaybolduğundan eminseniz,
    bu boş satırları tablodan tamamen silip atmak en mantıklı çözümdür. Çünkü bu kadar küçük bir veri kaybı,
    yapay zeka modelinizin başarısını veya istatistiksel sonuçlarınızı etkilemez.
    📌 Ne Zaman Kullanılır? (Şartlar Nelerdir?)Oran Çok Düşük Olmalı: Örneğin 10.000 satırlık şarap veri setiniz var.
    Sadece 20 satırda asitlik değeri girilmemiş. Bu oran %0.2 (binde iki) yapar. Doldurmaya çalışarak vakit kaybetmek
    yerine doğrudan silebilirsiniz.Rastgele Olmalı (MCAR): Eksikliğin arkasında sistemsel bir hata veya gizli bir neden olmamalıdır.
    🛠️ Python / Pandas ile Nasıl Yapılır?Pandas kütüphanesinde bu işlem için dropna() fonksiyonu kullanılır.
    İşte en sık kullanılan yöntemler:1. Tüm Satırı Silme (En Yaygın Yöntem)Eğer satırın içindeki herhangi bir sütun boşsa,
    o satırı tamamen siler:python# Eksik veri barındıran satırları siler ve df_temiz adında yeni bir tabloya aktarır
    df_temiz = df.dropna()

    # Eğer değişikliği mevcut tablonuzda kalıcı yapmak isterseniz:
    df.dropna(inplace=True)
    Kodu dikkatli kullanın.2. Sadece Belirli Sütundaki Boşluklara Göre Silme (subset)Tüm tablodaki boşluklar sizi ilgilendirmiyorsa,
    sadece kritik bir sütundaki (örneğin şarap veri setindeki alcohol sütunundaki) boş satırları silmek isteyebilirsiniz:
    python# Sadece alkol oranı boş olan satırları siler, diğer sütunlardaki boşluklara dokunmaz
    df.dropna(subset=["alcohol"], inplace=True)
    Kodu dikkatli kullanın.⚠️ Avantaj ve Dezavantajları Nelerdir?Avantajı: Çok hızlıdır, yapay zeka modeline uydurma veri (ortalama vs.)
    eklememiş olursunuz, tamamen gerçek verilerle çalışırsınız.Dezavantajı: Eğer eksik veri oranı %5'ten fazla olursa ve veri rastgele
    kaybolmadıysa (MAR veya MNAR), bu yöntem veri setinizi küçültür ve analizlerinizi yanlı/hatalı (biased) hale getirir.

B-) Imputation (Filling Missing Values)

    Imputation (Eksik Değerleri Doldurma), veri setindeki boş veya eksik (NaN) hücreleri silmek yerine, mantıklı ve tahmini
    değerlerle doldurma işlemidir.Veri biliminde satırları doğrudan silmek veri kaybına yol açtığı için, Imputation yöntemiyle
    tablonun bütünlüğü ve veri hacmi korunmuş olur.

    📌 En Sık Kullanılan Imputation Yöntemleri1. İstatistiksel Doldurma (Geleneksel Yöntemler)Sütunun genel karakterine bakarak boşlukları
    tek bir sabit sayı ile doldurursunuz:Ortalama (Mean) ile Doldurma: Sayısal sütunlarda boş yerlere o sütunun aritmetik ortalaması yazılır.
    Medyan (Median) ile Doldurma: Veride çok uç değerler (aykırı veri) varsa, ortalama yerine tam ortadaki değer (medyan) tercih edilir.
    Mod (Mode) ile Doldurma: Kategorik/metinsel sütunlarda (örneğin "Şehir" veya "Renk") boş yerlere en çok tekrar eden değer yazılır.
    2. Akıllı ve Gelişmiş Doldurma (Makine Öğrenmesi)Boşlukları doldururken diğer sütunlardaki ilişkileri de hesaba katarsınız:
    Gruplayarak Doldurma: Boş maaş verilerini tüm şirketin ortalamasıyla değil, kişinin sadece kendi departmanındaki ortalamayla doldurmak.
    KNN Imputer (En Yakın Komşular): Boş değere sahip satıra en çok benzeyen diğer satırları bulup, onların değerine göre bir tahmin yapar.

    🛠️ Python / Pandas ile Nasıl Yapılır?Pandas kütüphanesinde bu işlem için fillna() fonksiyonu kullanılır.A) Sabit Bir Değer veya Ortalama ile Doldurmapython# Tüm boşlukları 0 ile doldurur
    df_dolu = df.fillna(0)

    # Sadece 'alcohol' sütunundaki boşlukları o sütunun ortalamasıyla doldurur
    alkol_ortalamasi = df["alcohol"].mean()
    df["alcohol"].fillna(alkol_ortalamasi, inplace=True)
    Kodu dikkatli kullanın.B) Kategorik Sütunu Mod (En Çok Tekrar Eden) ile Doldurmapython# 'City' sütunundaki boşlukları en çok geçen şehirle doldurur
    en_cok_tekrar_eden = df["City"].mode()[0]
    df["City"].fillna(en_cok_tekrar_eden, inplace=True)
    Kodu dikkatli kullanın.C) Bir Önceki veya Sonraki Değerle Doldurma (Zaman Serileri)Hava durumu gibi peş peşe gelen verilerde,
    bugünün verisi eksikse dünün verisiyle doldurmak çok mantıklıdır:python# ffill (forward fill):
    Boşluğu bir üstteki (önceki) satırın değeriyle doldurur
    df["Sıcaklık"].fillna(method="ffill", inplace=True)
    Kodu dikkatli kullanın.⚖️ Avantaj ve DezavantajlarıAvantajı: Veri setinin boyutunu korursunuz.
    Veri kaybetmediğiniz için yapay zeka modelleri daha çok veriyle eğitilir.Dezavantajı:
    Eğer çok fazla veri doldurursanız verinin orijinal yapısını bozabilirsiniz. Yapay zeka modeline "uydurma" veri verdiğiniz için
    modelin gerçek hayattaki tahmin gücü düşebilir.


C-) Adding Missing Indicators

    Adding Missing Indicators (Eksik Veri Belirteci Ekleme), veri setindeki boş hücreleri doldurmadan önce,
    o verinin orijinalinde eksik olduğunu yapay zeka modeline bildirmek için yeni bir sütun (bayrak) ekleme yöntemidir.
    Bu yöntem özellikle verinin rastgele kaybolmadığı (MAR veya MNAR) durumlarda hayati önem taşır.
    📌 Neden İhtiyaç Duyarız? (Büyük Problem ve Çözümü)Problem: Bir sütundaki boşlukları ortalama (mean) ile doldurduğunuzda,
    yapay zeka modeli o satırların orijinalinde eksik olduğunu anlayamaz. Model, o verileri gerçekten "ortalama bir değere sahipmiş"
    gibi algılar ve arkadaki gizli kalıpları (örneğin cihazın neden bozulduğunu veya kişinin neden bilgi gizlediğini) kaçırır.
    Çözüm: Veriyi doldurmadan hemen önce yanına True/False veya 1/0 değerlerinden oluşan yeni bir sütun ekleriz.
    Böylece modele "Bak, ben bu veriyi ortalamayla doldurdum ama aslında orijinalinde bu veri yoktu, bunu hesaba kat!" mesajı vermiş oluruz.
    🛠️ Python / Pandas ile Nasıl Yapılır?Şarap veya hava durumu veri setinizdeki alcohol sütununda eksik veriler olduğunu varsayalım.
    Bu yöntemi adım adım şöyle uygularız:

    python import numpy as np
    import pandas as pd

    # 1. Adım: Belirteç (Indicator) sütununu oluşturuyoruz
    # Alkol sütunu boşsa 1 (True), doluysa 0 (False) yazar
    df["alcohol_was_missing"] = df["alcohol"].isna().astype(int)

    # 2. Adım: Orijinal sütundaki boşlukları ortalamayla dolduruyoruz
    alkol_ort = df["alcohol"].mean()
    df["alcohol"].fillna(alkol_ort, inplace=True)

    print(df[["alcohol", "alcohol_was_missing"]])
    Kodu dikkatli kullanın.Oluşan Yeni Tablo Görüntüsü:text    alcohol  alcohol_was_missing
    0     10.4                     0  # Zaten vardı, dokunulmadı.
    1     10.2                     1  # Orijinalde boştu (NaN), ortalamayla doldu ve fişlendi!
    2      9.5                     0  # Zaten vardı, dokunulmadı.
    Kodu dikkatli kullanın.⚙️ Scikit-Learn (Smarter Way) ile Otomatik YapmaEğer yapay zeka ve makine öğrenmesi aşamasına geldiyseniz,
    sklearn kütüphanesindeki SimpleImputer fonksiyonu bu işlemi add_indicator=True parametresiyle tek seferde otomatik olarak yapabilir:
    pythonfrom sklearn.impute import SimpleImputer

    # Hem ortalamayla doldur hem de otomatik olarak Missing Indicator sütunlarını ekle
    imputer = SimpleImputer(strategy="mean", add_indicator=True)
    df_transformed = imputer.fit_transform(df)
    Kodu dikkatli kullanın.⚖️ Avantaj ve DezavantajlarıAvantajı: Modelin veri kaybı arkasındaki sistemsel hataları
    (örneğin sensörün donmasını veya yüksek gelirlilerin veri gizlemesini) öğrenmesini sağlar, model başarısını ciddi oranda artırır.
    Dezavantajı: Veri setindeki sütun sayısını iki katına çıkarabilir. Eğer çok fazla sütununuz varsa, veri tablonuz aşırı genişler ve bilgisayarı
    yorabilir.


D-) Using Domain Knowledge

    Using Domain Knowledge (Alan Bilgisini Kullanmak), veri biliminde ham sayılar ve kodlar yerine, çalıştığın sektöre veya
    konuya ait uzmanlık bilgisini (tecrübeyi) kullanarak kararlar alma sürecidir.Veri biliminde sadece Python,
    Pandas veya makine öğrenmesi bilmek yetmez. Verinin geldiği alanı (tıp, finans, kimya, spor, meteoroloji vb.) anlamak,
    en doğru analizleri yapmanın anahtarıdır.Eksik verileri yönetirken alan bilgisinin nasıl hayat kurtardığını
    şu harika örneklerle anlayabiliriz:

    Alan Bilgisi (Domain Knowledge) Örnekleri1. Şarap Veri Setiniz Üzerinden (Kimya / Üretim Alanı)Diyelim ki şarap veri setinizde pH sütununda
    eksik veriler var.Sadece Kod Bilen Biri: Hemen df["pH"].fillna(df["pH"].mean()) yazıp tüm boşlukları genel ortalamayla doldurur.
    Alan Bilgisi Olan Biri: Şarabın pH değerinin, asitlik oranlarıyla (fixed acidity, citric acid) doğrudan kimyasal bir bağı olduğunu bilir.
    Boşlukları genel ortalamayla doldurmak yerine, şarabın türüne ve asitlik derecesine bakarak kimya kurallarına uygun bir tahminle doldurur
    veya uzman bir kimyagerden sınır değerleri öğrenir.2. Sağlık ve Tıp Alanı (Doktorluk Bilgisi)Bir hastane veri setinde hastaların
    Hamilelik Sayısı sütunu boş bırakılmış olsun.Sadece Kod Bilen Biri: Sütunun ortalamasını alır (örneğin 1.5 çıkar) ve boş yerlere 1.5 yazar.
    Alan Bilgisi Olan Biri: Yan sütundaki Cinsiyet bilgisine bakar. Eğer hastanın cinsiyeti Erkek (M) ise, alan bilgisi ona bir erkeğin hamile
    kalamayacağını söyler. Bu yüzden o boşlukları ortalamayla değil, doğrudan 0 ile doldurur.3. Olimpiyat Veri Setiniz
    Üzerinden (Spor Alanı)Sporcuların Medal (Madalya) sütununda binlerce NaN (boş veri) görmüştünüz.Sadece Kod Bilen Biri:
    "Aaa burada çok fazla eksik veri var, veri setinin %80'i boş!" diyerek bu sütunu silebilir veya "Gold/Silver" ile doldurmaya çalışabilir.
    Alan Bilgisi Olan Biri: Olimpiyat kurallarını bilir. Yarışmalarda sadece ilk 3'e girenlere madalya verilir; geri kalan yüz binlerce sporcu
    yarışı madalyasız tamamlar. Yani orardaki NaN değerleri bir "hata veya eksiklik" değil, "madalya kazanamadı" anlamına gelen çok değerli bir bilgidir.
    Bu yüzden o boşlukları silmez, df["Medal"].fillna("No Medal") yaparak anlamlı hale getirir.⚖️ Neden Bu Kadar Önemlidir?Hatalı Modelleme Engellenir:
    Yapay zekaya mantıksız veya doğaya aykırı veriler (örneğin hamile erkek verisi veya kimyasal olarak imkansız bir şarap pH değeri) vermenizi engeller.
    Doğru Özellik Mühendisliği (Feature Engineering): Hangi sütunların birbiriyle ilişkili olduğunu matematiksel korelasyondan önce mantıksal olarak
    bilmenizi sağlar.Veri biliminde en başarılı modeller, algoritmayı çok iyi bilen yazılımcılar ile o işin sektör uzmanlarının (doktorlar,
    mühendisler, ekonomistler) alan bilgisini birleştirdiği anlarda ortaya çıkar.

"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df)

print(df.isnull().sum())  # eksik verilerin sayısını bulduk
"""
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
"""
# Burada encok eksik kolonun deck olduğu gözlemlendi


print(df.shape)  # toplam satır ve sütuu bulduk
"""
(891, 15)
"""

# 1-) EKSİK VERİLERİ SİLME

print(df.dropna().shape)  # eksik veriler atıldı
"""
(182, 15)
"""
# eksik veriler atılınca satır alanında ciddi veriler eksildiğini görüyoruz
# bu tercih edilen bir durum değil çünkü çok fazla veriler siliniyor

print(df.dropna(axis=1)) # eksik verilerin olduğu kolon siliniyor
# Burada kolonda bir tane bile eksik veri olmuş olsa bütün kolonu silecek
# o yüzden çok tercih edilen bir durum değil


# 2-) EKSİK VERİERİ DOLDURMA (IMPUTATION)

# 2.1-) Mean Imputation

print(df.isnull().sum())
"""
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64

Burada age doldurmaya çalışacağız
"""
sns.histplot(data=df["age"], kde=True)

df["Age_mean"] = df["age"].fillna(df["age"].mean())
print(df[["Age_mean","age"]])
"""
      Age_mean   age
0    22.000000  22.0
1    38.000000  38.0
2    26.000000  26.0
3    35.000000  35.0
4    35.000000  35.0
..         ...   ...
886  27.000000  27.0
887  19.000000  19.0
888  29.699118   NaN
889  26.000000  26.0
890  32.000000  32.0

Burada ortalama koyulduğunda eski verilerin yerinde olduğu ve boş verilerin
ortalama ile dolduğu gözlemlenmektedir
"""

"""
NOT --> Neden ortalama alıyoruz medyan yada daha farklı birşey koyamazmıydık.
        Bunu anlamak için,
        Çok fazla autlayır varsa medyan koymak daha fazla mantıklı
        data normal dahılıma benziyorsa ortalamayı koymak mantıklıdır
        mod daha çok kategorik veriler için yapılır
        
"""

sns.boxplot(data=df, y="age") # burada outlayır görebiliriz


# 2.2-) Median
df["age_median"] = df["age"].fillna(df["age"].median())

print(df[["age","age_median","Age_mean"]])

"""
      age  age_median   Age_mean
0    22.0        22.0  22.000000
1    38.0        38.0  38.000000
2    26.0        26.0  26.000000
3    35.0        35.0  35.000000
4    35.0        35.0  35.000000
..    ...         ...        ...
886  27.0        27.0  27.000000
887  19.0        19.0  19.000000
888   NaN        28.0  29.699118
889  26.0        26.0  26.000000
890  32.0        32.0  32.000000

[891 rows x 3 columns]
"""

# 2.3-) Mode 

print(df[df["embarked"].isnull()]) # boş olan satırları görüyoruz
"""
     survived  pclass     sex   age  sibsp  parch  fare embarked  class  \
61          1       1  female  38.0      0      0  80.0      NaN  First   
829         1       1  female  62.0      0      0  80.0      NaN  First   

       who  adult_male deck embark_town alive  alone  Age_mean  age_median  
61   woman       False    B         NaN   yes   True      38.0        38.0  
829  woman       False    B         NaN   yes   True      62.0        62.0  
"""

df[df["embarked"].notna()] # sadece dolu olanları getiriyor
"""


survived	pclass	sex	age	sibsp	parch	fare	embarked	class	who	adult_male	deck	embark_town	alive	alone	Age_mean	age_median
0	0	3	male	22.0	1	0	7.2500	S	Third	man	True	NaN	Southampton	no	False	22.000000	22.0
1	1	1	female	38.0	1	0	71.2833	C	First	woman	False	C	Cherbourg	yes	False	38.000000	38.0
2	1	3	female	26.0	0	0	7.9250	S	Third	woman	False	NaN	Southampton	yes	True	26.000000	26.0
3	1	1	female	35.0	1	0	53.1000	S	First	woman	False	C	Southampton	yes	False	35.000000	35.0
4	0	3	male	35.0	0	0	8.0500	S	Third	man	True	NaN	Southampton	no	True	35.000000	35.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
886	0	2	male	27.0	0	0	13.0000	S	Second	man	True	NaN	Southampton	no	True	27.000000	27.0
887	1	1	female	19.0	0	0	30.0000	S	First	woman	False	B	Southampton	yes	True	19.000000	19.0
888	0	3	female	NaN	1	2	23.4500	S	Third	woman	False	NaN	Southampton	no	False	29.699118	28.0
889	1	1	male	26.0	0	0	30.0000	C	First	man	True	C	Cherbourg	yes	True	26.000000	26.0
890	0	3	male	32.0	0	0	7.7500	Q	Third	man	True	NaN	Queenstown	no	True	32.000000	32.0
889 rows × 17 columns
"""

df[df["embarked"].notna()]["embarked"].mode()
"""
Burada embarked modunu bulduk
0    S
Name: embarked, dtype: str
"""

mode_value = df[df["embarked"].notna()]["embarked"].mode()[0]
print(mode_value)
# S

df["embarked_mode"] = df["embarked"].fillna(mode_value)
print(df[["embarked","embarked_mode"]])
"""
    embarked embarked_mode
0          S             S
1          C             C
2          S             S
3          S             S
4          S             S
..       ...           ...
886        S             S
887        S             S
888        S             S
889        C             C
890        Q             Q

[891 rows x 2 columns]
"""

print(df["embarked"].isnull().sum()) # 2

print(df["embarked_mode"].isnull().sum()) # 0



