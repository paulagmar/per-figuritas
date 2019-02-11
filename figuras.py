import math
class shape():
    def __init__(self):
        pass

    def area(self):
        return self.area
    def perimetro(self):
        return self.perimetro

class cuadrado(shape):
    def __init__(self,lado):
        self.lado=lado
    def area(self):
        area=(lado*self.lado)
        return area
    def perimetro(self):
        perimetro=(4*self.lado)
        return perimetro

class rectangulo(shape):
    def __init__(self, lado1,lado2):
        self.lado1=lado1
        self.lado2=lado2

    def area(self):
        area=(self.lado1*self.lado2)
        return area
    def perimetro(self):
        perimetro=(self.lado1*2+self.lado2*2)
        return perimetro

r=rectangulo(4,2)
print(r.area(), r.perimetro())

class circulo(shape):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        area=(math.pi*self.radio**2)
        return area

    def perimetro(self):
        perimetro=(2*math.pi*self.radio)
        return perimetro

class elipse(shape):
    def __init__(self,semiejemayor, semiejemenor):
        self.semayor=semiejemayor
        self.semenor=semiejemenor

    def area(self):
        area=(math.pi*self.semayor*self.semenor/4)
        return area

    def perimetro(self):
        perimetro=(2*math.pi*((self.semayor**2+self.semenor**2)/2)**0.5)
        return perimetro
 
