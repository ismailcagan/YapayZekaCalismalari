dosya = open("deneme.txt","w")
"""
Ne işe yarar? Bu satır, "deneme.txt" adında bir dosyayı yazma ("w" - write)
modunda açar.Önemli Özellikleri:Eğer "deneme.txt" dosyası klasörde yoksa, 
sıfırdan yeni bir dosya oluşturur.Eğer bu dosya zaten varsa, 
içerisindeki tüm eski verileri tamamen siler ve boş bir dosya olarak açar.
Bu yöntemle dosya açtığınızda, işiniz bittiğinde arkasından mutlaka dosya.close() 
kodunu yazarak dosyayı kapatmanız gerekir.
"""


with open("deneme.txt","w",encoding="UTF-8") as dosya:
    dosya.write("Merhaba Bu Veri Dosyaya Yazılıyor_1")
"""
Ne işe yarar? Bu, yukarıdaki yöntemin daha modern, 
güvenli ve profesyonel halidir.Önemli Özellikleri:with yapısı 
(Context Manager), içerisindeki işlemler bittiği an dosyayı 
otomatik olarak kapatır. Sizin manuel olarak dosya.close() 
yazmanıza gerek kalmaz.Kod çalışırken bir hata (exception) 
oluşsa bile dosyanın güvenle kapatılmasını garanti eder, 
sistem kaynaklarını korur.
"""
