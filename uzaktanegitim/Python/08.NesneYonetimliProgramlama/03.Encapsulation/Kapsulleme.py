# encapsulation

# semi private attributes
class A():
    def __init__(self):
        self.a = "Normal"
        self._b = "Korumalı"
    
class B(A):
    def __init__(self):
        self.b = "Normal"
        A.__init__(self)
        

# private attributes