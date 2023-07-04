'''
Creamos un entorno virtual python 3.11.3 : Desde la consola..
  Jeferson@DESKTOP-VJM2PL1 MINGW64 /e/cursos_python/POO_Python_Edteam_2023 (main)
  $ py -m venv venv

  Jeferson@DESKTOP-VJM2PL1 MINGW64 /e/cursos_python/POO_Python_Edteam_2023 (main)
  $ source venv/Scripts/activate
  
  Jeferson@DESKTOP-VJM2PL1 MINGW64 /e/cursos_python/POO_Python_Edteam_2023 (main)
  $ pip install cryptocode
  Collecting cryptocode
    Downloading cryptocode-0.1-py3-none-any.whl (4.1 kB)
  Collecting pycryptodomex
    Downloading pycryptodomex-3.18.0-cp35-abi3-win_amd64.whl (1.7 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 13.8 MB/s eta 0:00:00
  Installing collected packages: pycryptodomex, cryptocode
  Successfully installed cryptocode-0.1 pycryptodomex-3.18.0

  [notice] A new release of pip available: 22.3.1 -> 23.1.2
  [notice] To update, run: python.exe -m pip install --upgrade pip
  (venv) 
'''
from cryptocode import encrypt,decrypt
from abc import ABC, abstractclassmethod

class UsuarioBase(ABC):
  def __init__(self,nombre, apellido, correo, contrasenia, telefono):
    self.nombre = nombre,
    self.apellido = apellido,
    self.correo = correo,
    self.contrasenia=self.encriptarContrasenia(contrasenia),
    self.telefono=telefono
    
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
    
Usuario1 = UsuarioConcreto(
      ombre="Jeferson",
      apellido="Dextre",
      correo="jadex@gmail.com",
      contrasenia="test",
      telefono="926464164"
)

print(Usuario1.contrasenia)
print(Usuario1.verificarContrasenia("test"))