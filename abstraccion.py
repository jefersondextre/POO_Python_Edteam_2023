from cryptocode import encrypt, decrypt
# abc clase que permite agregar la abstraccion a la clase 
from abc import ABC, abstractmethod
# CLASE PADRE
class UsuarioBase(ABC):
  
  def __init__(self,nombre, apellido, correo, contrasenia, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.telefono = telefono
  
  # el decorador es una funcion que engloba a la funcion y le da 
  # caracteristicas adicionales imprlementadas en el metodo con decorador @abstracmetod
  # 
  @abstractmethod
  def encriptarContrasenia(self,contrasenia):
    pass
    
  @abstractmethod
  def verificarContrasenia(self, contrasenia):
    pass 


# = CLASE HIJA ==========================================================
# Los metodos estan creando la estructura en la clase base para que la clase hija 
# implemente tanto el metodo pero que le agregue la funcionalidad correcta en cada una de ellas.
class UsuarioConcreto(UsuarioBase):
  
    def encriptarContrasenia(self,contrasenia):
      # token_super_seguro, es nuestro token de seguridad
      # contrasenia es la contraseña que queremos encriptar
      return encrypt(contrasenia,"token_super_seguro")
    
    def verificarContrasenia(self, contrasenia):
      contrasenia_desencriptada = decrypt(self.contrasenia,"token_super_seguro")
      return contrasenia_desencriptada == contrasenia
    
usuario1 = UsuarioConcreto(
      nombre="Jorge",
      apellido="Vasquez",
      correo="jvasquez@gmail.com",
      contrasenia="test",
      telefono=9264644564,
)
print(usuario1.contrasenia)
print(usuario1.verificarContrasenia("test"))

# jdextre@SMARITIMA08 MINGW64 /c/EDteam/POO_Python_Edteam_2023 (main)
# $ py abstraccion.py
# qDQzCQ==*7SBDw+KVJiKVzxMhdekL5g==*xBbDqLwyXfxR6xCXxZX91A==*YS9/KegFXBFZJSi5FbmsHQ==
# True
# (venv) 
# jdextre@SMARITIMA08 MINGW64 /c/EDteam/POO_Python_Edteam_2023 (main)
# $ py abstraccion.py
# JIobEQ==*xjkKKoKsugEjMcy3aCGsaA==*NLfIWRILTXtjM4iexqNeSw==*G4BZwvUKx/OMUai/U5aNXw==
# False
# (venv) 
# 
# 
# 