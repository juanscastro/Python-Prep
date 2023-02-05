# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

#           0           1       2           3
ciudad = ['Kosovo', 'Quito', 'Cochamo', 'Punta Arenas', 'Islas Sandwich']
print(ciudad)

# 2) Imprimir por pantalla el segundo elemento de la lista

print(ciudad[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento

print(ciudad[1:4])

# 4) Visualizar el tipo de dato de la lista

type(ciudad)

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(ciudad[2:])

# 6) Visualizar los primeros 4 elementos de la lista

print(ciudad[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

ciudad.append('Kosovo')
ciudad.insert(5, 'Manila')
# 8) Agregar otra ciudad, pero en la cuarta posición

ciudad.insert(3, 'Kabul')

# 9) Concatenar otra lista a la ya creada

ciudad.extend(['Ecuador', 'Chile'])

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

print(ciudad.index('Kabul'))

# 11) ¿Qué pasa si se busca un elemento que no existe?

print(ciudad.index('Kabula'))

# 12) Eliminar un elemento de la lista

ciudad.remove('Kosovo')

# 13) ¿Qué pasa si el elemento a eliminar no existe?

ciudad.remove('Helsinky')

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

last = ciudad.pop()
print(last)

# 15) Mostrar la lista multiplicada por 4


len(ciudad)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

tupla = tuple(ciudad)

# 17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

20 and 30 in tupla
'Cochamo' in tupla

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
paris = 'Paris'
if not paris in ciudad:
    ciudad.append(paris)
    print('Paris se agrega en Ciudad')

    print(ciudad)

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

tupla.count('Kosovo')
ciudad.count('Kosovo')

# 21) Convertir la tupla en una lista

tuplalista = list(tupla)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables


ciudad1, ciudad2, ciudad3 = tupla[0], tupla[1], tupla[2]
print('ciudad1:', ciudad1)
tupla[:2]


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

diccionario = {'Ciudad': ciudad}
diccionario['Pais'] = 'Argentina', 'Ecuador', 'Chile'
print(diccionario)
# 24) Imprimir las claves del diccionario

print(diccionario.keys())

# 25) Imprimir las ciudades a través de su clave -->

print(diccionario['Ciudad'])
