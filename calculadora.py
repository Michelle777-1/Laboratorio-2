from Todos_los_modulos import funciones_calculadora
opcion = 1
while opcion != 9:
    print("MENÚ DE OPCIONES")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Potencia")
    print("6. Raíz")
    print("7. Factorial")
    print("8. Conversion (radiones y grados)")
    print("9. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print("La suma es: ", funciones_calculadora.suma())
    elif opcion == 2:
        print("La resta es: ", funciones_calculadora.resta())
    elif opcion == 3:
        print("La dvisión es: ", funciones_calculadora.división())
    elif opcion == 4:
        print("La multiplicación es: ", funciones_calculadora.multiplicación())
    elif opcion == 5:
        print("La potencia es: ", funciones_calculadora.potencia())
    elif opcion == 6:
        print("La raíz cuadrada es: ", funciones_calculadora.raiz())
    elif opcion == 7:
        print("El factorial es: ", funciones_calculadora.factorial_función())
    elif opcion == 8:
        print("La conversión es: ", funciones_calculadora.conversion())
    elif opcion == 9:
        print("Fin")
    else:
        print("Opción no válida")
