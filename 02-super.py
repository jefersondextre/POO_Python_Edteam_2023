class Mascota:
  def __init__(self,nombre):
    self.nombre = nombre
    
  def juega(self):
    print(f"La mascota {self.nombre} esta jugando")
    
class Perro(Mascota):
  def __init__(self,nombre,raza):
    super().__init__(nombre)
    self.raza=raza
  
  def juega(self):
    super().juega()
    print(f"El perro de raza {self.raza} juega con su hueso")
    
class PerroDomestico(Perro):
  def __init__(self,nombre,raza,propietario):
    super().__init__(nombre, raza)
    self.propietario = propietario
    
  def juega(self):
    super().juega()  
    print(f"El perrodomestico mueve la cola")
  
  def presentarse(self):
    print(f"Hola soy {self.nombre} de raza {self.raza} y mi dueño es {self.propietario}.")
    
    

perroDomestico = PerroDomestico(
  nombre = "Firulais",
  raza="Samoyedo",
  propietario="Antonio"
)

perroDomestico.presentarse()
perroDomestico.juega()