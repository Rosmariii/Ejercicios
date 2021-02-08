class Triángulo():
    def __init__(self, ladoA, ladoB, ladoC):
            self.ladoA = ladoA
            self.ladoB = ladoB
            self.ladoC = ladoC

    def LadoLargo(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print(f'El lado A es el de mayor tamaño {self.ladoA}')
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print(f'el lado B es el de mayor tamaño {self.ladoB}')
        else:
            print(f'El lado C es el de mayor tamaño {self.ladoC}')

    def TipoTriángulo(self):
        if self.ladoA == self.ladoB & self.ladoB == self.ladoC:
            print('Este triángulo es de tipo Équilatero')
        elif self.ladoA == self.ladoB or self.ladoB == self.ladoC or self.ladoA == self.ladoC:
            print('Este triángulo es de tipo Isóseles')
        else: 
            print('Este triángulo es de tipo Escaleno') 

while(True):
    try: 
        lA = (int(input('Ingrese el tamaño del lado A del triangulo: ')))
        lB = (int(input('Ingrese el tamaño del lado B del triangulo: ')))
        lC = (int(input('Ingrese el tamaño del lado C del triangulo: ')))
        break
    except:
        print("Ha ocurrido un error, introduce bien el número entero")

unTriángulo = Triángulo(lA,lB,lC)

print(unTriángulo.LadoLargo())
print(unTriángulo.TipoTriángulo())



#git add .
#git commit -m ""
#git push