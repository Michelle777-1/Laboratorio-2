import math
def suma():
    a = float(input("Ingrese número:"))
    b = float(input("Ingrese número:"))
    suma = a+b
    return suma
def resta():
    a = float(input("Ingrese número:"))
    b = float(input("Ingrese número:"))
    resta = a-b
    return resta
def división():
    a = float(input("Ingrese número:"))
    b = float(input("Ingrese número:"))
    if b == 0:
        print("Error. No se puede dividir entre 0")
    else: 
        división = a/b
    return división
def multiplicación():
    a = float(input("Ingrese número:"))
    b = float(input("Ingrese número:"))
    mult = a*b
    return mult
def potencia():
    a = float(input("Ingrese número:"))
    b = int(input("Ingrese número:"))
    potencia = a**b
    return potencia
def raiz_cuadrada():
    a = float(input("Ingrese número:"))
    if a>=0:
        return math.sqrt(a)
    else:
        print( "Error. No existe raíz de número negativo")
def factorial_función():
    a = float(input("Ingrese número:"))
    factorial = math.factorial(a)
    return factorial
def conversion():
    print("Opción de conversión")
    print("1. Grados")
    print("2. Radianes")
    opción = int(input("Ingrese opción"))
    if opción == 1:
        num = int(input("Ingrese número a convertir:"))
        grados = math.degrees(num)
        return grados
    elif opción == 2: 
        num = int(input("Ingrese número a convertir:"))
        radianes = math.radians(num)
        return radianes
    else:
        print("No está en las opciónes")
