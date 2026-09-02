import numpy as np
import matplotlib.pyplot as plt

# 1-) TEMEL GRAFİK OLUŞTURMA

age_list = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]

weight_list = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]

plt.plot(age_list, weight_list, "r")
plt.show()
plt.savefig("test.png")  # kaydetmek için kullanılır


plt.plot(age_list, weight_list, "r")
plt.title("Age vs Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 2-) NUMPY DİZİLERİNDE GRAFİK OLUŞTURMA

age_list = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
weight_list = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]


np_age_list = np.array(age_list)
print(np_age_list)  # [10 20 30 30 30 40 50 60 70 75]

np_weight_list = np.array(weight_list)
print(np_weight_list)  # [20 60 80 85 86 87 70 90 95 90]

plt.plot(np_age_list, np_weight_list, "r")
plt.title("Age vs Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()
# ------------------------------------------------------------------

numpy_arr1 = np.linspace(0, 10, 20)
print(numpy_arr1)
"""
[ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.63157895
  3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368
  6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842
  9.47368421 10.        ]
"""
numpy_arr2 = numpy_arr1**3
print(numpy_arr2)
"""
[0.00000000e+00 1.45793847e-01 1.16635078e+00 3.93643388e+00
 9.33080624e+00 1.82242309e+01 3.14914711e+01 5.00072897e+01
 7.46464499e+01 1.06283715e+02 1.45793847e+02 1.94051611e+02
 2.51931768e+02 3.20309083e+02 4.00058318e+02 4.92054235e+02
 5.97171599e+02 7.16285173e+02 8.50269719e+02 1.00000000e+03]
"""

plt.plot(numpy_arr1, numpy_arr2, "b")
plt.show()

plt.plot(numpy_arr1, numpy_arr2, "b*")
plt.show()

plt.plot(numpy_arr1, numpy_arr2, "b*-")
plt.show()

plt.plot(numpy_arr1, numpy_arr2, "b--")
plt.show()

plt.plot(numpy_arr1, numpy_arr2, "b+")
plt.show()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3-) BİRDEN FAZLA GRAFİGI YAN YANA ÇİZME

plt.subplot(1, 2, 1)
plt.plot(numpy_arr1, numpy_arr2, "r*-")
plt.subplot(1, 2, 2)
plt.plot(numpy_arr2, numpy_arr1, "g--")
plt.show()

# 4-) KENDİ GRAFİĞİMİZİ OLUŞTURMA

my_figure = plt.figure()
figure_axes = my_figure.add_axes([0.1, 0.1, 0.3, 0.3])
figure_axes.plot(numpy_arr1, numpy_arr2, "g")
figure_axes.set_xlabel("X Axis")
figure_axes.set_ylabel("Y Axis")
figure_axes.set_title("Graph Title")
plt.show()

"""
Bu yöntem, grafik penceresini ve grafiğin çizileceği alanı birer "nesne" (kutu) olarak ele alır. Şöyle düşünebilirsin: plt.figure() ile boş bir resim tuvali satın alıyorsun, add_axes() ile de bu tuvalin üzerine resim yapacağın çerçevelerin yerini ve boyutunu çiziyorsun.Kodlarını adım adım ve içindeki parametrelerin ne anlama geldiğini net bir şekilde açıklayayım.Bölüm 1: add_axes Mantığı ve İlk Grafikpythonmy_figure = plt.figure()
Kodu dikkatli kullanın.Anlamı: Bilgisayarın hafızasında tamamen boş, beyaz bir tuval (pencere) oluşturur.pythonfigure_axes = my_figure.add_axes([0.1, 0.1, 0.3, 0.3])
Kodu dikkatli kullanın.Anlamı: Bu tuvalin içine bir grafik ekseni (çerçevesi) ekler.İçindeki Sayılar ([sol, alt, genişlik, yükseklik]) Ne Demek? Bu sayılar tuvalin genişlik ve yüksekliğine oranla (0 ile 1 arasında) konum belirler:0.1: Soldan %10 boşluk bırak.0.1: Alttan %10 boşluk bırak.0.3: Grafiğin genişliği tuvalin %30'u kadar olsun.0.3: Grafiğin yüksekliği tuvalin %30'u kadar olsun (Yani küçük bir grafik alanı oluşturmuşsun).pythonfigure_axes.plot(numpy_arr1, numpy_arr2, "g")
Kodu dikkatli kullanın.Anlamı: Oluşturduğun bu küçük çerçevenin içine verileri çizer. "g" parametresi çizginin renginin yeşil (green) olacağını söyler.pythonfigure_axes.set_xlabel("X Axis")
figure_axes.set_ylabel("Y Axis")
figure_axes.set_title("Graph Title")
Kodu dikkatli kullanın.Anlamı: Eksen yönteminde başlık ve isimler verilirken başlarına set_ kelimesi gelir. Sırasıyla X ekseni adı, Y ekseni adı ve Grafiğin ana başlığı eklenir.
"""


new_fig = plt.figure(dpi=100)  # dpi -> boyutu ayarlıyor
new_axes = new_fig.add_axes([0.1, 0.1, 0.9, 0.9])
new_axes.plot(numpy_arr1, numpy_arr1**2, label="numpy array **2")
new_axes.plot(numpy_arr1, numpy_arr1**3, label="numpy array **3")
new_axes.legend(
    loc=1
)  # çzgilerin hangi anlama geldiğini gçsteren resmi oluşturuyor. loc=1 konumunu belirtiyor
plt.show()

"""
Bölüm 2: DPI, Aynı Grafikte Çoklu Çizim ve Legend (Lejant)pythonnew_fig = plt.figure(dpi=100)
Kodu dikkatli kullanın.Anlamı: Yeni bir boş tuval açar. dpi=100 (Dots Per Inch), grafiğin çözünürlüğünü ve kalitesini belirler. 
Sayı büyüdükçe grafik daha net, keskin ve büyük görünür.pythonnew_axes = new_fig.add_axes([0.1, 0.1, 0.9, 0.9])
Kodu dikkatli kullanın.Anlamı: Bu sefer tuvali kaplayacak daha büyük bir grafik alanı açtın (Genişlik ve yükseklik %90 yapılmış).
pythonnew_axes.plot(numpy_arr1, numpy_arr1 ** 2, label="numpy array **2")
new_axes.plot(numpy_arr1, numpy_arr1 ** 3, label="numpy array **3")
Kodu dikkatli kullanın.Anlamı: Aynı grafik alanının (new_axes) içerisine iki farklı çizgi çiziyorsun.
label Parametresi: Çizgilerin üzerine isim etiketi yapıştırır. "Bu mavi çizgi karesini gösteriyor, 
bu turuncu çizgi küpünü gösteriyor" demek gibidir.pythonnew_axes.legend(loc=1)
Kodu dikkatli kullanın.Anlamı: Grafiklerin üzerinde label ile belirttiğin isimlerin yazdığı 
o küçük bilgilendirme kutusunu (lejant) ekrana basar.loc=1 Parametresi: Bu kutunun grafiğin neresinde duracağını söyler
:loc=1: Sağ Üst Köşe (Upper Right)loc=2: Sol Üst Köşe (Upper Left)loc=3: Sol Alt Köşe (Lower Left)loc=4: Sağ Alt Köşe (Lower Right)

Neden Bu Yöntemi Kullanıyoruz?"Neden düz plt.plot() yazıp geçmiyoruz?" 
diye düşünebilirsin. Bu nesne yönelimli yöntemin en büyük avantajı, 
iç içe (grafik içinde grafik) tasarımlar yapabilmektir.Örneğin; 
büyük bir grafiğin tam sağ alt köşesine küçük bir grafik daha 
sıkıştırmak istersen add_axes ile konumları ayarlayarak bunu kolayca yapabilirsin.
Bir sonraki adımda tek bir tuval üzerinde yan yana veya alt alta 2-3 farklı 
grafik açmayı sağlayan plt.subplots() konusuna geçmek ister misin, 
yoksa bu kodlardaki koordinatları (add_axes sayılarını) değiştirmeyi mi deneyelim?
"""

# 5-) MATPLOTLİB STİLLERİ

data1 = np.linspace(0, 10, 20)
data2 = data1**2

my_fig, my_axes = plt.subplots()
my_axes.plot(data1, data2, color="#1e0703", alpha=0.5)
my_axes.plot(data2, data1, color="#53ca0a")
plt.show()


new_fig, new_axes = plt.subplots()
new_axes.plot(data1, data1 + 2, color="blue", linewidth=1)
new_axes.plot(data1, data1 + 4, color="yellow", linewidth=4)
new_axes.plot(data1, data1 + 6, color="red",linestyle="-." )

new_axes.plot(data1, data1 + 8, color="#000000",linestyle="-",
              marker="o", markersize = 8, markerfacecolor="red")

# 6-) FARKLI GRAFİK ÇEŞİTLERİ

# Scatter
plt.scatter(data1,data2)
plt.show()

#Histogram
plt.hist(data1)
plt.show()
#-----------------------------------------------

new_arr = np.random.randint(0,100,50)
plt.hist(new_arr)
plt.show()

#box plot
plt.boxplot(data1)
plt.show()

