respuesta = True

while (respuesta):
    x = int(input('Ingrese un numero a evaluar : '))
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
    pregunta = input('Para continuar, escriba yes, para salir escriba no : ')
    if (pregunta == 'no'):
        break
