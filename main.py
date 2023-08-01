# Ejemplo de una clase

class Usuario():
    # Datos (Atributos)
    def __init__(self,nombre, apellido,correo,contrasenia,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia= contrasenia
        self.telefono = telefono
    
    # Funcionalidad (Metodos)
    def encriptarContrasenia(self):
        return "Encriptando....! "
    
    def verificarContrasenia(self):
        return "Desencriptando"

Usuario1 = Usuario( nombre="Jeferson",
                    apellido="Dextre",
                    correo="jadexb04@gmail.com",
                    contrasenia="test20",
                    telefono="926949164"
)

# print(Usuario())
# print(Usuario1)

# Usuario1.nombre
# Usuario1.encriptarContrasenia()

# Usuario1.nombre= "kevin"
# Usuario1.apellido= "Guzmán"
print("Usuario #1")
print("="*10)
print(Usuario1.nombre)
print(Usuario1.apellido)
# print(Usuario1.encriptarContrasenia())

Usuario2 = Usuario( nombre="Jon",
                    apellido="Doe",
                    correo="jon@gmail.com",
                    contrasenia="2355",
                    telefono="956223214"
)
# Usuario2.nombre="Carlos"
# Usuario2.apellido="Fernandez"
print("Usuario #2")
print("="*10)
print(Usuario2.nombre)
print(Usuario2.apellido)

print(Usuario2.encriptarContrasenia())