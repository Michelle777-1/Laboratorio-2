from Todos_los_modulos import funcionesComparacion
from Todos_los_modulos.funcionesIngreso import es_un_numero
def mostrar_menu():
    print("MENÚ DE OPCIONES")
    print("1. Hallar el máximo de 2 valores")
    print("2. Hallar el mínimo de 2 valores")
    print("3. Comprobar si son iguales")
    print("4. Comprobar si son diferentes")
    print("5. Ingresar un valor y validar si es número")
    print("6. Salir")
def menu():
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            opciones(1)
        elif opcion == 2:
            opciones(2)
        elif opcion == 3:
            opciones(3)
        elif opcion == 4:
            opciones(4)
        elif opcion == 5:
            opciones(5)
        elif opcion == 6:
            print("Fin")
        else:
            print("Opción no válida")
def opciones(opcion):
    if opcion == 1:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("Máximo:", funcionesComparacion.maximo(a, b))
    elif opcion == 2:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("Mínimo:", funcionesComparacion.minimo(a, b))
    elif opcion == 3:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("¿Son iguales?:", funcionesComparacion.iguales(a, b))
    elif opcion == 4:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("¿Son diferentes?:", funcionesComparacion.diferentes(a, b))
    elif opcion == 5:
        valor = input("Ingrese un valor:")
        es_un_numero(valor)
