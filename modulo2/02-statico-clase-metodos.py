class MiClase:
    atributo_de_clase= 7
    def __init__(self,color):
        self.color = color
    
    # Metodo estatico no tiene acceso a ningun atributo de la clase
    @staticmethod
    def metodo_estatico(color):
        print(f"Este es un metodo estático del color {color}") 

    # Metodo 
    @classmethod
    def metodo_de_clase(cls):
        print(cls.__name__)
        print("Este es un metodo estático con el atributo de clase...",cls.atributo_de_clase) 
    
miclase = MiClase("Yellow")

miclase.metodo_estatico('green')
# miclase.metodo_estatico()
# miclase.metodo_de_clase()
MiClase.metodo_estatico('Orange')
MiClase.metodo_de_clase()