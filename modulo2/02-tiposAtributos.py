  # (1) atributos de clase : Son compartidos de forma general
  # para todas las instancias de la clase.
  # (2) atributos de instancias: Son diferentes para cada una 
  # de las instancias que le asigna valores.
  # (3) atributos de datos: Son unicos para la instancia en la
  # que se crea y se inicializa.
class Vehiculo:
    # Atributos de clase
  ruedas = 4  # (1)
  
  # Atributos de instancia (2)
  def __init__(self, marca, modelo, velocidad, anio):
    self.marca     = marca
    self.modelo    = modelo
    self.velocidad = velocidad
    self.anio      = anio
  
    
  # metodos
  def darVelocidad(self, velocidad):
    self.velocidad += velocidad

  def reducirVelocidad(self, velocidad):
    self.velocidad -= velocidad
    
vehiculo1 = Vehiculo("ford",2022,20,2023) #(2)
print("="*10)
print("Instancia 1")
print('instancia 1 - ruedas: ',vehiculo1.ruedas) #(2)
# print(vehiculo1.marca)
# print(vehiculo1.modelo)
# print(vehiculo1.velocidad,"km/h")
# print(vehiculo1.anio)

# vehiculo1.ruedas=6  # No podemos reasignar atributos desde la instancia ❌. 
# Ya que de este modo solo estamos haciendo un cambio a la copia de ruedas
Vehiculo.ruedas = 6    # Reasignando atributos desde la clase, logra que todas
# las instancias reflejen este nuevo valor, este cambio. ✅

vehiculo2 = Vehiculo("Mazda",2020,40,2023)
print("="*10)
print("Instancia 2 : ")
print('instancia 2 - ruedas:',vehiculo2.ruedas)
print('instancia 1 - ruedas:',vehiculo1.ruedas)
# print(vehiculo2.marca)
# print(vehiculo2.modelo)
# print(vehiculo2.velocidad," km/h")
# print(vehiculo2.anio)

# Atributos de datos, esto solo estara en esta instancia 
vehiculo2.color = 'Black'
print('==== vehiculo 2 - color =====')
print(vehiculo2.color)