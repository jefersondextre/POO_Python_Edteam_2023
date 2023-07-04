from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class UsuarioBase(ABC):
  
  def __init__(self,nombre, apellido, correo, contrasenia, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.telefono = telefono
    
  @abstractmethod
  def encriptarContrasenia(self,contrasenia):
    pass
    
  @abstractmethod
  def verificarContrasenia(self, contrasenia):
    pass 
  
class UsuarioConcreto(UsuarioBase):
    def encriptarContrasenia(self,contrasenia):
      return encrypt(contrasenia,"secret")
    
    def verificarContrasenia(self, contrasenia):
      contrasenia_desencriptada = decrypt(self.contrasenia,"secret")
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
