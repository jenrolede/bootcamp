class Dino:
    ojos = 2
    def __init__(self,un_nombre, un_color, canti_patas=4, un_genero=None):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas 
        self.genero = un_genero
        #self.despedida = una_despedida
        print("naci")

    def saludar(self):
        print("hola me llamo", self.nombre, "tengo", self.patas,"patas y soy", self.genero)

    def cortar_patas(self, cantidad_de_patas_a_cortar=1):
        self.patas = self.patas - cantidad_de_patas_a_cortar

    def decir_genero(self):
        print("hola soy", self.nombre, "y me identifico como", self.genero)

    #def despedirce_fin(self):
      #  print("hola soy", self.nombre, "y me identifico como", self.genero, self.despedida )


barney = Dino("rex", "marron", 6, "macho")
print(barney.nombre)
barney.saludar()
barney.decir_genero()
barney.cortar_patas()
print(barney.patas)
barney.saludar()

proto = Dino("Lira", "rosa", 8, "hembra")
print(proto.nombre)
proto.saludar()
proto.decir_genero()
proto.cortar_patas(2)
proto.saludar()



