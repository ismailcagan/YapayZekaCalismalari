"""
Slicing --> belirlenen aralıklardaki indeksleri alma

degisken[staring index : stopping index : stepping size ]
degisken[başlama indeksi : duracağı index : kaçar adımda ileleyecek]
"""

barkod = "ABC123456965"
barkodİlkUc = barkod[:3:]
print(barkodİlkUc) # ABC

barkodİkiAdimAtla = barkod[::2]
print(barkodİkiAdimAtla) # AC2466

barkodTersCevir = barkod[::-1]
print(barkodTersCevir) # 569654321CBA



