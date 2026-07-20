"""
Dosyalama işlemleri;
Metin Tabanlı -> txt,csv,json,xml
Bınary
olarak ikiye ayrılır
Burada Metin Tabanlı Olanı işleyeceğiz
dosyayı açmak için kullanılan fonksiyon open() fonksiyonudur.
open(
    "C:\Dosyalar\dosya.txt",
    "dosya.txt",
    "r"
)
    "r" -> okumak için dosyayı açar ön tanımlımoddur
    "w" -> yazmak için dosyayı açar dosya bu modda açıldığında var olan içeriği siler yeni dosya oluşturur
    "a" -> yazmak içindosya açar dosyanın önceden oluşturulmuş olması gerekir
    "r+" -> dosyanın önceden oluşturulması gerekir. bu mod hem okumak hem yazmak için kullanılır
    
    Dosyaları oluşturmak için 3 farklı metot vardır.
    read() -> parametre olarak byte değeri alır, byte değeri verilemdiğinde dosyanın tamamını alır
    readline() -> dosyanın içindeki satırları birer birer okur
    readlines() ->  Tüm satırları okuyarak bize bir liste şeklide verir
    
    Dosyaları Yazmak için 2 farklı metot vardır
    write() -> içeriği direk yazar
    writelines() -> satır satır yazar
    
    Dosya Okuma Sırasında İmleçler Kullanılır. 
    dosya okunduğunda bu imleç başa alınmaz dosyada bulunduğumuz yeri bilmek dosyanın içinde 
        istediğimiz yere gidebilmek için farklıfonksiyonlara ihtiyaç duyarız Bunlar;
        seek() ve tell() fonksiyonlarıdır.
        seek() ve tell() fonksiyonları, dosya işlemleri sırasında imlecin (dosya işaretçisinin)
        konumunu yönetmek ve takip etmek için kullanılır. Dosya okuma veya yazma adımlarını 
        kontrol etmenizi sağlarlar.
        tell(): İmlecin o anda dosyanın kaçıncı bayt (byte) konumunda olduğunu söyler.
        seek(): İmleci dosya içinde istediğiniz belirli bir bayt konumuna taşır.
        
    Dosyaya yazım işlemini ardından bilgilerini kaydedilmesi gerekir bunun için dosyanın kapatılması
        veriyi kaydetmek için yeterlidir Bunun için close() kullanılır.
        Farklı olarak dosyamızı kaydedip çalışmaya devam ette ihtiyacı duyduğumuzda flush() fonksiyonu kullanırız
        flush(): Geçici bellekteki (tampon) verileri hemen diske yazar, ancak dosyayı açık tutmaya devam eder.
        close(): Önce içerideki flush() fonksiyonunu otomatik çağırıp tüm verileri diske kaydeder, 
            ardından dosyayı tamamen kapatır.
"""
