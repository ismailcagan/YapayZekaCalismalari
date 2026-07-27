import sys
print(*sys.path,sep="\n") # python'un bir modülü (kütüphaneyi) çağırırken (import ederken) hangi klasörlere sırasıyla bakacağını gösteren yolları listeler.

# Python'un arama listesine geçici olarak yeni bir klasör yolu ekler.
sys.path.append("/home/ares/Desktop/Yazilimlar/YapayZeka/UzaktanEgitim/Python/01.ilkProjem/") # 
# Yukarıda eklenen klasör içindeki ilkProgram.py isimli dosyayı bir modül gibi kodunuza dahil eder.
import ilkProgram.py

"""
sys.version_info: Kullanılan Python sürümünü detaylı olarak verir.
.major: Ana sürüm (Örn: 3)
.minor: Alt sürüm (Örn: 11)
.micro: Yama sürümü (Örn: 2)
"""
print(sys.version_info.major,sys.version_info.minor,sys.version_info.micro)
# Kodun çalıştığı işletim sistemi platformunu gösterir (Örn: Linux için 'linux', Windows için 'win32').
print(sys.platform)
"""
Programı terminalden çalıştırırken yanına yazdığınız argümanları 
(parametreleri) bir liste olarak alır. 
listenin ilk elemanı her zaman programın kendi adıdır.
"""
print(sys.argv)

"""
Eğer programı terminalde python kod.py versionCheck şeklinde 
çalıştırdıysanız, bu koşul sağlanır ve ekrana Python sürümünü 
aralarında çizgi olacak şekilde (Örn: 3-11) yazdırır.
"""
if "versionCheck" in sys.argv:
    print(sys.version_info.major,sys.version_info.minor,sep="-")

"""
sys.getdefaultencoding(): Python'un karakterleri (metinleri) 
belleğe yazarken varsayılan olarak hangi kodlamayı (utf-8 vb.) 
kullandığını gösterir.sys.getrecursionlimit(): 
Python'da bir fonksiyonun kendi kendini en fazla kaç kez üst üste 
çağırabileceğini (öz yineleme / yineleme sınırı) gösterir. 
Varsayılan sınır genellikle 1000'dir.
sys.setrecursionlimit(5000): Sınırı 5000'e yükseltir.
Son satırdaki sys.getrecursionlimit() ise sınırın başarıyla 
5000 olup olmadığını kontrol etmek için tekrar ekrana yazdırır.
"""
print(sys.getdefaultencoding())
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(5000))
print(sys.getrecursionlimit())