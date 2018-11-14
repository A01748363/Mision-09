# Autor: David Isaí López Jaimes


def extraerPares(lista):
    lista2 = []
    for valor in lista:
        lista2.append(valor)
        if valor%2 != 0:
            lista2.remove(valor)
    return lista2


def extraerMayoresPrevio(lista):
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


def intercambiarMM(lista):

    lista.remove(max(lista))
    lista.remove(min(lista))
    lista.append(min(lista))
    lista.append(max(lista))
    return lista



def promediarCentro(lista):
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


def calcularEstadistica(lista):
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


def calcularSuma(lista):
    pass


def main():
    lista = [1,2,3]
    promedio = promediarCentro(lista)
    print(promedio)

    a = intercambiarMM(lista)
    print(a)


main()