class Vehiculo:
  # aributos
  def __init__(self, marca, modelo, velocidad, anio):
    self.marca = marca,
    self.modelo = modelo,
    self.velocidad = velocidad,
    self.anio = anio
  # metodos
  def darVelocidad(self, velocidad):
    self.velocidad += velocidad

  def reducirVelocidad(self, velocidad):
    self.velocidad -= velocidad
  
class Motocicleta(Vehiculo):
  def __init__(self, marca, modelo, velocidad, anio, motor):
    super().__init__(marca,modelo,velocidad,anio)
    self.motor = motor
  
  # Hacer caballito
  def Wheelie(self):
    return "Haciendo el wheelie....🐎 !!"
  
class Autobus(Vehiculo):
  def __init__(self, marca, modelo, velocidad, anio, asientos):
    super().__init__(marca, modelo, velocidad, anio)
    self.asientos= asientos
   
    
  def cargarPasajeros(self,pasajeros=30):
    return f"Pasajeros a bordo: {pasajeros} pasajeros."
  
  

# motocicleta = Motocicleta("Honda","2021",100,2023,1200)
# print(motocicleta.marca)
# print(motocicleta.Wheelie())

autobus=Autobus("Blubird",2010,velocidad=100,anio=2023,asientos=30)
print(autobus.modelo)
print(autobus.cargarPasajeros(62))