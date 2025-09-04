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
    if a>=0:
        return math.sqrt(a)
    else:
        print( "Error. No existe raíz de número negativo")
def factorial_función():
    a = float(input("Ingrese número:"))
    factorial = math.factorial(a)
    return factorial
def conversion():
    a = float(input("Ingrese número:"))
    b = float(input("Ingrese número:"))
    suma = a+b
    return suma
