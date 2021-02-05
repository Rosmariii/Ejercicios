class vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def Descripcion(self):
        return f'El vehiculo es de color {self.color} y tiene {self.ruedas} ruedas'

class  coche(vehiculo):
    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def detalles(self):
        return f'El coche tiene una velocidad de {self.velocidad} km/h y una cilindrada de {self.cilindrada} CC'

x = vehiculo('negro', 4)
y = coche(160, 1.6)

print(x.Descripcion())
print(y.detalles())
