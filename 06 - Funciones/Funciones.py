
# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
numero = int(input("inserte numero: "))


def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
        else:
            primo = True
    return primo

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números
#  y devuelva sólo aquellos que son primos en otra lista


numero = [1, 2, 3, 4, 5, 6, 7, 23]
primos = []


def filterPrimo(numero):
    for i in numero:
        if i < 3:
            primos.append(i)
        else:
            for n in range(2, i):
                if i % n == 0:
                    primo = False
                    break
                else:
                    primo = True
            if (primo):
                primos.append(i)
            else:
                primo = False
    return primos


filterPrimo(numero)

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite
#  y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

lista = [1, 2, 3, 2, 3, 3, 4, 4, 4, 5, 6, 4]
mayor = True


def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    if (mayor):
        moda = lista_unicos[1]
        maximo = lista_repeticiones[1]
    return moda, maximo


valor_modal(lista)

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

grados = 0
medidaor = "C"
medidadest = "K"


def conversor(grados, medidaor, medidadest):
    if medidaor == "C" and medidadest == "F":
        print("Convirtiendo", grados, medidaor, "a", medidadest)
        convertido = 32 + (grados * 9 / 5)
    elif medidaor == "C" and medidadest == "K":
        print("Convirtiendo", grados, medidaor, "a", medidadest)
        convertido = grados + 272.15
    return convertido


conversor(0, "C", "K")


# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:


# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo


def factorial(x):
    acumulado = 1

    if x <= 0 or type(x) != int:
        print("por Favor, ingrese un numero entero positivo mayor a uno")
    else:
        while x > 1 and type(x) == int:
            acumulado = acumulado * x
            x -= 1
    return acumulado


factorial(5)


def thing():
    print("Hello")


x = 5


print(acumulado)
