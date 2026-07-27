class Deneme:
    
    def __init__(self,limit):
        self.limit = limit
    
    def __iter__(self):
        self.a = 5
        return self
    
    def __next__(self):
        a = self.a
        
        if a > self.limit:
            raise StopIteration
        self.a = a+1
        return a
    
for i in Deneme(10):
    print(i)
"""
5
6
7
8
9
10
"""

#-------------------------------------------------------------------

metin = "python egitimi"
for i in metin:
    print(i)
"""
p
y
t
h
o
n
 
e
g
i
t
i
m
i
"""
