  # (1) atributos de clase : Son compartidos de forma general para todas las instancias de la clase.
  # (2) atributos de instancias: Son diferentes para cada una de las instancias que le asigna valores.
  # (3) atributos de datos: Son unicos para la instancia en la que se crea y se inicializa.
class Vehiculo:
  ruedas = 4  # (1)
  
  def __init__(self, marca, modelo, velocidad, anio):
    self.marca = marca,
    self.modelo = modelo,
    self.velocidad= velocidad,
    self.anio = anio
  # metodos
  def darVelocidad(self, velocidad):
    self.velocidad += velocidad

  def reducirVelocidad(self, velocidad):
    self.velocidad -= velocidad

vehiculo1 = Vehiculo("ford",2022,20,2023) #(2)
print("Instancia 1")
print("="*10)
print(vehiculo1.ruedas)
print(vehiculo1.marca)
print(vehiculo1.modelo)
print(vehiculo1.velocidad)
print(vehiculo1.anio)

vehiculo1.ruedas=6  # No podemos hacer
Vehiculo.ruedas=8 

vehiculo2 = Vehiculo("Mazda",2020,40,2023)
print("Instancia 2")
print("="*10)
print(vehiculo2.ruedas)
print(vehiculo1.ruedas)
print(vehiculo2.marca)
print(vehiculo2.modelo)
print(vehiculo2.velocidad)
print(vehiculo2.anio)