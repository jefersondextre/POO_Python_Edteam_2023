class MainMenu:
    # Para el uso del menu principal
    @staticmethod
    def showMainMenu():
        print("""
            *************************************
            ***** EDTEAM - PYTHON CONTACTS ******
            *************************************
            1. Añadir contacto.
            2. Listar contactos.
            3. Buscar contacto.
            4. Editar contacto.
            5. Cerrar aplicacion.
            """)
        option = int(input("Seleccione una opción: "))
        while option > 5 or option < 1: 
            print("opción no valida.")
            option = int(input("Seleccione una opcion nuevamente: "))
        else:
            return option
        
    @staticmethod
    def showMenuAddContact():
        print("""
        ******************
        Añadir contacto
        ******************
        """)
        
    @staticmethod
    def addContact():
        name  = input("Ingrese su nombre: ")
        email = input("Ingrese su correo: ")
        phone = input("Ingrese su telefono: ")
        return name,email,phone
        
    @staticmethod   
    def showMenuAllContacts():
        print("""
        **********************************************
        *********** Lista de contactos ***************
        ********************************************** """)
        print("Nombre    |    correo    |    Telefono")

    @staticmethod
    def showMenuSearchContact():
        print("""
        ******************
        Buscar contacto
        ******************""")
    
    @staticmethod  
    def searchContact():
        email = input("Ingrese correo de contacto: ")
        return email
    
    @staticmethod
    def showMenuUpdate():
            print("""
        ******************
        Editar contacto
        ******************""")
            
    @staticmethod
    def getContactEmail():
        return input("Ingrese el correo de contacto: ")
    
    @staticmethod
    def getContactDate():
        name= input("Ingrese nombre de contacto: ")
        phone= input("Ingrese telefono de contacto: ")
        return name, phone
    
        
    