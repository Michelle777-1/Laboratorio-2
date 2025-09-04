from Módulos.mensajes import enviar_msj, ver_mensajes
from Módulos.contactos import contacto, lista_contactos
def iniciar_chat():
    if not contacto:
        print("No tiene contactos, agrega uno")
        return
    lista_contactos()
    nombre=input("Escriba el nombre del contacto con el que quiere iniciar un chat: ")
    if nombre not in contacto:
        print("Ese contacto no existe")
        return
    while True:
        print("---Chat con ",nombre,"---")
        print("1 Enviar mensaje")
        print("2 Ver mensajes")
        print("3 Volver al menú")
        opcion=int(input("Seleccione opción: "))
        if opcion==1:
            texto=input("Escriba su mensaje: ")
            enviar_msj(nombre,texto)
        elif opcion==2:
            ver_mensajes(nombre)
        elif opcion==3:
            break
        else:
            print ("Opción no válida")
