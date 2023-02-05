# Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

var1 = 3
if var1 != 0:
    print(var1)

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

var2 = 3
var3 = 'Juan'
if type(var2) == type(var3):
    print('Son el mismo tipo de dato!')
else:
    print('No son el mismo tipo de dato')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range(1, 21):
    if n % 2 == 0:
        print(str(n) + ' es Par')
    else:
        print(str(n) + ' Es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for n in range(0, 6):
    print(n ** 3)
    n += 1

# 5) Crear una variable que contenga un número entero y
# realizar un ciclo for la misma cantidad de ciclos

vars = 4
for i in range(vars):
    print('ciclo!')

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable,
# sólo si la variable contiene un número entero mayor a 0
# 5 x 4 x 3 x 2 x 1

x = 5
acumulado = 1

while x > 1 and type(x) == int:
    acumulado = acumulado * x
    x -= 1
print(acumulado)

# 7) Crear un ciclo for dentro de un ciclo while

x = int(input('Inserte num: '))
while x < 5:
    for i in range(x):
        print('Hola!')
    x = x + 1

# 8) Crear un ciclo while dentro de un ciclo for
x = 1
for i in range(x):
    while x == 1:
        print(x)

# 9) Imprimir los números primos existentes entre 0 y 30
# 1,2,3,5,7,11,13,25,27
# primos = 1, 2, 3, 5, 7, 11, 17, 19, 23, 29

# topederango = 30
# n = 3


#     for i in range(2, n):
#         if n % i == 0:
#             print(str(n) + 'No es primo')
#     else:
#         print(str(n) + 'Es primo')
#     n = n + 1


# i i i i i i i
# 1 2 3 4 5 6
# 1 2 3 4 5 5
#   1 2 3 4 5
#     1 2 3 4
#       1 2 3
#         1 2
#           1 2
# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

#  Se redujo la cantidad de evaluaciones al llegar al valor False

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
# si
# 13) Aplicando continue, armar un ciclo while que solo imprima los
# valores divisibles por 12, dentro del rango de números de 100 a 300


# n = 100
# while n < 300:
#     if n % 12 != 0:
#         n = n + 1
#         continue
#     else:
#         print(n)
#         n = n + 1


# n = 100
# while n < 300:
#     if n % 12 == 0:
#         print(n)
#     n = n + 1


# i = 0
# while i < 9:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# Skip the iteration if the variable i is 3, but continue with the next iteration:


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente


respuesta = True

while (respuesta):
    x = int(input())
    primo = True
    for i in range(2, x):
        if x % i == 0:
            primo = False
            break
    if (primo):
        print('Es primo!')
    else:
        print('No es primo!')
        # preguntamos si quiere ingresar otro valor
    pregunta = input()
    if (pregunta == 'no'):
        break


# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while n < 300:
    if n % 3 == 0 and n % 6 == 0:
        print(n)
        break
    n = n + 1
