from contactos import *
from mensajes import *
from chats import *
opcion = 1
while opcion != 4:
    print("---WHATSAPP---")
    print("1. Contactos")
    print("2. Mensajes")
    print("3. Chats")
    print("4. Salir")
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        opcion2 = 1
        while opcion2 != 4:
            print("---WHATSAPP---")
            print("1. Agregar contacto")
            print("2. Eliminar contacto")
            print("3. Ver contactos")
            print("4. Volver al menú")
            opcion2 = int(input("Eliga una opción:"))
            if opcion2 == 1:
                agregar_contacto()
            elif opcion2 == 2:
                eliminar_contacto()
            elif opcion2 == 3:
                lista_contactos()
            elif opcion2 == 4:
                print("Volviendo al menú principal")        
    elif opcion == 2:
        opcion3 = 1
        while opcion3 != 3:
            print("---WHATSAPP---")
            print("1. Enviar mensaje")
            print("2. Ver mensaje")
            print("3. Volver al menú")
            opcion3 = int(input("Eliga una opción:"))
            if opcion3 == 1:
                lista_contactos()
                nombre = input("Ingrese el nombre del contacto:")
                if nombre in contacto:
                    texto = input("Ingrese mensaje:")
                    enviar_msj(nombre,texto)
                else:
                    print("Ese contacto no existe")
            elif opcion3 == 2:
                lista_contactos()
                nombre = input("Ingrese el nombre del contacto:")
                if nombre in contacto:
                    ver_mensajes(nombre)
                else:
                    print("Ese contacto no existe")
            elif opcion3 == 3:
                print("Volviendo al menú principal")
    elif opcion == 3:
        print("-----WHATSAPP-----")
        print("Ingresando a chats")
        iniciar_chat()    
    elif opcion == 4:
            print("saliendo")
