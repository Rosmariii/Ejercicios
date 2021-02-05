class pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo {}".format(self.nombre, self.tipo)

#unPoquemon = pokemon('asd','rojo')
#print(unPoquemon.descripcion())

class pikachu(pokemon):
    def ataque(self, tipoDeAtaque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoDeAtaque)

class charmander(pokemon):
    def ataque(self, tipoDeAtaque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoDeAtaque)

nuevoPokemon = pikachu('picachu', 'electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('impactrueno'))
