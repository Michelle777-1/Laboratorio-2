contacto = {}
def agregar_contacto():
    nombre = input("Ingrese nombre del nuevo contacto:")
    numero = input("Ingrese número del contacto:")
    if len(numero) <9:
        numero = input("Agrege número de telefono completo")
    contacto[nombre] = int(numero)
    return print ("Contacto agregado")
def eliminar_contacto():
    nombre = input("Ingrese nombre del contacto ha eliminar:")
    if nombre in contacto:
        contacto.pop(nombre)
    else:
        print("Ese contacto no existe")
def lista_contactos():
    print("--------Contactos--------")
    for nombre,numero in contacto.items():
        print(f"{nombre}: {numero}")
    return contacto
    