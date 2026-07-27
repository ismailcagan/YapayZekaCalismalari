import platform as pf

# Linux-7.0.0-107027-tuxedo-x86_64-with-glibc2.43
print(pf.platform()) # işletim sistemi hakkında bilgi verir

# Linux-7.0.0-107027-tuxedo-x86_64-with-glibc2.43
print(pf.platform(0,1))

# x86_64
print(pf.machine()) # 32 bit mi 64 bitmi bunu verir

print(pf.processor())

# ('64bit', 'ELF')
print(pf.architecture())

# Linux
print(pf.system()) # işletim sisteminin adı

# #27tux1 SMP PREEMPT_DYNAMIC Wed Jul  8 15:31:58 UTC 2026
print(pf.version()) # işletim sistemi versionunu verir


import webbrowser as web

web.open("www.python.org")

print(dir(web))


# builter modül listesi öğrenme
import sys
print(sys.builtin_module_names)

import pkgutil
print(*pkgutil.iter_modules(),sep="\n")


import os

