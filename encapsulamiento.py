
class Usuario:
    def __init__(self, nombre, apellido, contrasenia, correo, telefono):
        # atributos publicos
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.correo = correo
        # atributos privados
        self.__telefono = telefono

    def obtener_telefono(self):
        return self.__telefono

    def actualizar_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

    def encriptarContrasenia(self, contrasenia):
        pass

    def verificarContrasenia(self, contrasenia):
        pass


# =========
usuario1 = Usuario(
                  nombre = "Jeferson",
                  apellido = "Dextre",
                  correo = "jadex.dev@gmail.com",
                  contrasenia = "test",
                  telefono = "1234")

print(usuario1.apellido)
print(usuario1.actualizar_telefono('926949162'))
print(usuario1.obtener_telefono())
usuario1.__telefono='5678'  # NO MODIFICA EL ATRIBUTO (2)
# print(usuario1.__telefono)   # GENERA ERROR (1)

# cONCLUSIONES
'''
CONCLUSIONES
============
(1)(2) No podemos acceder ni modificar atributos privados desde cualquier instancia de una clase


'''
