
class Usuario:
    def __init__(self, nombre, apellido, contrasenia):
        # atributos publicos
            self._nombre      = nombre
            self._apellido    = apellido
            self._contrasenia = self.encriptarContrasenia(contrasenia)
        # self._correo      = correo
        # # atributos privados
        # self.__telefono = telefono
    
    def encriptarContrasenia(self,contrasenia):
        pass
    
    def verificarContrasenia(self,contrasenia):
        pass
    
    # GETTER: @property Decorador es una función que recibe como argumento a otra función y le agrega nuevas funcionalidades
    @property
    def get_nombre(self):
        return self._nombre 

    # SETTER:       
    @get_nombre.setter
    def set_nombre(self,nombre):
        self._nombre = nombre
			
    @property
    def get_apellido(self):
        return self._apellido
    
    @get_apellido.setter
    def set_apellido(self,apellido):
      self._apellido = apellido

      
usuario1 = Usuario(
  nombre      = "Jeferson",
  apellido    = "Dextre",
  contrasenia = "test"
  )

print(usuario1.get_nombre)
print(usuario1.get_apellido)
usuario1.set_nombre   = "Antonio"
usuario1.set_apellido = "Barrientos"
print(usuario1.get_nombre)
print(usuario1.get_apellido)
