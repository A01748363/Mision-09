# Autor: David Isaí López Jaimes
# Programa que hace distintas funciones con listas


def extraerPares(lista):    # Función que recibe lista y regrasa una nueva con solo los numeros pares de la original
    lista2 = []
    for valor in lista:
        lista2.append(valor)
        if valor%2 != 0:
            lista2.remove(valor)
    return lista2


def extraerMayoresPrevio(lista): # Funcion que imprime los mayores previos a la lista anterior
    lista2 = []
    for dato2 in lista:
        numero = dato2
        break
    for dato in lista:
        if dato > numero:
            lista2.append(dato)
            numero = dato
        else:
            numero = dato
    return lista2


def intercambiarParejas(lista):
    pass


def intercambiarMM(lista):      # Funciòn que intercambia la posiciòn del mayor y menor de una lista
    lista2 = []
    for dato in lista:
        if dato == max(lista):
            lista2.append(min(lista))
        elif dato == min(lista):
            lista2.append(max(lista))
        else:
            lista2.append(dato)
    return lista2


def promediarCentro(lista):  # Funciòn que promedia los valores de una lista, pero sin el minimo y maximo
    listaPromedio = []
    for dato in lista:
        listaPromedio.append(dato)
    if len(listaPromedio) == 0 or len(listaPromedio) == 2 or len(listaPromedio) == 1:
        promedio = 0
    else:
        listaPromedio.remove(max(listaPromedio))
        listaPromedio.remove(min(listaPromedio))
        promedio = sum(listaPromedio)//len(listaPromedio)

    return promedio


def calcularEstadistica(lista):     # Funciòn que calcula la media y la desviaciòn estandar de una función
    desviacion = 0
    if len(lista) > 0:
        media = sum(lista)/len(lista)
        for dato in lista:
            desviacion+= (dato-media)**2
        desviacionT = desviacion/(len(lista)-1)
        desviacionTotal2 = desviacionT**0.5

    else:
        media = 0
        desviacionTotal2 = 0

    return media,desviacionTotal2


def calcularSuma(lista):   # Funcion que suma todos los elementos de una lista, menos el numero 13, el numero anterior y porterior de este
    for dato in lista:
        if dato == 13:
            lista.pop(lista.index(13)+1)
            lista.pop(lista.index(13)-1)
            lista.pop(lista.index(13))
    suma = sum(lista)

    return suma

