# Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

lista = []
i = -15
while i < 0:
    lista.append(i)
    i += 1
print(lista)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

i = -15
while i < 0:
    if i % 2 == 0:
        print(lista[i])
    i += 1

# 3) Resolver el punto anterior sin utilizar un ciclo while

for n in lista:
    if n % 2 == 0:
        print(n)

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

for n in lista:
    if n < lista[3]:
        print(n)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

for i, c in enumerate(lista):
    print(i, c)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

lista = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]
for c, i in enumerate(lista):
    if i < 21 and c != i:
        lista.insert(c, c)

print(lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

lista = []
nant1 = 0
nant2 = 1

for n in range(0, 31):
    if n == 0:
        lista.append(nant1)
    elif n == 1:
        lista.append(nant2)
    else:
        nact = (nant1) + (nant2)
        nant1 = nant2
        nant2 = nact
        lista.append(nact)
print(lista)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
# f0 f1 f2 f3 f4 f5
# 0 1 1 3 5 7

# 8) Realizar la suma de todos elementos de la lista del punto anterior

print(sum(lista))

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618…
# que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci.
# Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>

# ni-1/ ni
# ni-2/ ni-1
# ni-3/ ni-2
# ni-4/ ni-3
# ni-5/ ni-4


ult = lista[-1]
antult = lista[-2]

for i in lista:
    if len(lista)-i < 5:
        print(ult / antult)
        ult = antult
        antult = lista[-2-i]

for i in range(-5, 0):
    a = lista[i]
    b = lista[i-1]
    print(a/b)

#                                               print(lista[30]) = b
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

# print(lista[-2])
# print(len(lista))                                   b = len(list)
#                                            a  print(lista[b

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for c, i in enumerate(cadena):
    if i == 'n':
        print(c, i)

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

mi_dict = {'a', 'b', 'c'}
for i in mi_dict:
    print(i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador

listacadena = list(cadena)
for i in listacadena:
    print(i)

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
listatuple1 = tuple(lista1)
listatuple2 = tuple(lista2)
zipped = zip(listatuple1, listatuple2)

print(tuple(zipped))


print(tuple(zip(lista1, lista2)))

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lista = []
lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
for i in lis:
    if i % 7 == 0:
        lista.append(i)
print(lista)


# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene,
#  teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>

lis = [[1, 2, 3, 4], 'rojo', 'verde', [
    True, False, False], ['uno', 'dos', 'tres']]
elementos = 0
for i in lis:
    if type(i) == str:
        elementos = elementos + 1
    else:
        elementos = elementos + len(i)

print(elementos)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

lis = [[1, 2, 3, 4], 'rojo', 'verde', [
    True, False, False], ['uno', 'dos', 'tres']]

# for i in lis:
#     if type(i) != list:
#         elemalista = list(i)
#         lis.extend(elemalista)
#         lis.remove(i)

nuevaLis = []

for c in lis:
    if type(c) != list:
        posLis = list(c)
        print(posLis)
        nuevaLis.append(posLis)
    else:
        nuevaLis.append(c)
print(nuevaLis)
print(list('rojo'))

listaa = [1, 2, 3]
listab = [4, 5, 6]
listaa.insert(2, listab)
print(listaa)

lis = [[1, 2, 3, 4], 'rojo', 'verde', [
    True, False, False], ['uno', 'dos', 'tres']]

new_lis = []
for c in lis:
    if type(c) != list:
        posLis = list(c)
    else:
        posLis = c
    new_lis.append(posLis)

lis = new_lis
print(lis)

# Agregar un elemento especificando el índice
#  >>> mi_lista.insert(3,'Negro')
#  >>> print(mi_lista[:])
# ['Rojo', 'Azul', 'Amarillo', 'Negro', 'Naranja', 'Violeta', 'Verde']
