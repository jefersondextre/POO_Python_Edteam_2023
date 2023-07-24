from menu import MainMenu
from contacts import Contacts

if __name__ == '__main__':
    while True:
        option   = MainMenu.showMainMenu() # Muestra el menu principal de opciones
        contacts = Contacts() # convierto la clase Contacts() en contacts
        match(option):
            case 1: # AGREGAR CONTACTOS
                MainMenu.showMenuAddContact() # Muestra el titulo Añadiendo contacto
                # print(MainMenu.addContact(...))
                name, email, phone = MainMenu.addContact() # Recibe los tres valores, datos de contacto y los guarda en variables.
                contacts.add(name, email, phone) # Envio los argumentos para ser añaditos y agregados a la lista de contactos
            case 2: # LISTAR CONTACTOS  
                MainMenu.showMenuAllContacts() # Muestra el encabezado de los datos a recibir de los contactos
                contacts.show_all_contacts() # Imprime todos los contactos de la lista.
            case 3: # BUSCAR CONTACTOS 
                MainMenu.showMenuSearchContact() # Imprime el encabezado buscar contacto
                email = MainMenu.searchContact() # Recibe el email del contacto a buscar  
                print(email)
                contact = contacts.search(email) 
                
                if contact:
                    print(contact)
                else:
                    print("El contacto no existe")
                
            case 4: # update contact
                MainMenu.showMenuUpdate() # Muestra encabezado de actualizar editar contacto
                MainMenu.showMenuAllContacts() # Encabezado de todos los contactos
                contacts.show_all_contacts() # Muestra lista de contactos de la lista
                email   = MainMenu.searchContact() # Recibe el email del contacto a editar
                contact = contacts.search(email) # Busca el contato por su email recibido.
                if contact :
                    name,phone = MainMenu.getContactDate() # Recibe datos que faltan: nombre y telefono de contacto identificado por el email para editar.
                    resp  = contacts.update(contact["email"],name,phone) # Actualizando contacto
                    print("Contacto actualizado.")
            case 5: # close app
                print("Hasta luego")
                break