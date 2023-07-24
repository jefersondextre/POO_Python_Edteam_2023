class Vehiculo:

    def __init__(self, marca, modelo): 
        self.marca     = marca
        self.modelo    = modelo
        self.velocidad = 0

    def darVelocidad( velocidad):  # se accede siempre a traves de la clase
        # self.velocidad += velocidadf
        print(velocidad)
        
    #  self es un objeto que hace referencia a todo el contenido de la clase
    def reducirVelocidad(self,velocidad):   # se accede siempre a traves de una instancia
        self.velocidad -= velocidad
        print(self.velocidad)
        
vehiculo1 = Vehiculo("ford","2020")
# print(vehiculo1.marca)
# print(vehiculo1.modelo)

# vehiculo1.reducirVelocidad(-20)
# vehiculo1.darVelocidad(20)  # ❌ Esto no funciona esta funcion esa recibiendo 2 paametros pero solo debe recibir 1 , ya que solo es una funcion.
# Vehiculo.darVelocidad(20)    # ✅
# Vehiculo.reducirVelocidad(vehiculo1,25)
print(vehiculo1.reducirVelocidad)
print(Vehiculo.reducirVelocidad)