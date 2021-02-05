class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def Caracteristicas(self):
        return f'Estas son las las Caracteristicas de Coche:\n velocidad {self.velocidad} km/h\n cilindrada: {self.cilindrada} \n color: {self.color} \n rueda: {self.ruedas}' 
        


class Camioneta(Coche):
    def __init__(self, velocidad, cilindrada, carga, color, ruedas): 
        Coche.__init__(self, color, ruedas, velocidad, cilindrada) 
        self.carga = carga

    def Caracteristicas(self):
        return f'Estas son las las Caracteristicas de Camioneta:\n velocidad {self.velocidad} km/h \n cilindrada: {self.cilindrada} \n color: {self.color} \n rueda: {self.ruedas}' 
        
#class Bicicleta(Vehiculo):
#    def __init__(self, tipo):
#        self.tipo = tipo

#class Motocileta(Bicicleta):
#    def otraDes(self, tipo, velocidad, cilindrada, color, ruedas):
#        Bicicleta.__init__(self, tipo, color, ruedas)
#        self.velocidad = velocidad
#        self.cilindrada = cilindrada

v1 = Coche('Rojo', '19', '210', '2.0')
v2 = Camioneta('290', '2.2', '250', 'Blanco', '20')
#v3 = Bicicleta('deportiva', 'negro', 17)
#v4 = Motocileta('deportiva', 120, 600, 'Blanco', 17)

transporte = [v1, v2]

# def Catalogar(listVehiculo, xruedas = None):
#     if xruedas == transporte.ruedas:
#         print(transporte)
        
#     else:
#         for vehiculo in listVehiculo:
#             print(vehiculo.Caracteristicas())

def Catalogar(listVehiculo, xruedas = None):
    if xruedas == None:
        for vehiculo in listVehiculo:
            print(vehiculo.Caracteristicas())
    
    else:
        countVehiculo = 0
        ruedasEncontradas = 0

        for vehiculo in listVehiculo:
            if vehiculo.color == xruedas:
                countVehiculo = countVehiculo + 1
                ruedasEncontradas = xruedas
        
        print(f"Se han encontrado {countVehiculo} vehículos con {ruedasEncontradas} ruedas:")               
        
Catalogar(transporte, '19')
        