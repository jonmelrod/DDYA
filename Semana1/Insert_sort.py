#Menor a mayor y Mayor a menor


import matplotlib.pyplot as plt

def asce(m, lista):
    lista =[]
    for n in m:
        lista.append(int(n))
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = clave

    print("La secuencia ordenada de menor a mayor es:", lista)
    return lista

def desce(m, lista):
    lista =[]
    for n in m:
        lista.append(int(n))
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] < clave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = clave

    print("La secuencia ordenada de mayor a menor es:", lista)
    return lista


def graficar(lista, orden):
    plt.plot(lista, marker="o")
    plt.title("Lista " + orden)
    plt.xlabel("Posicion")
    plt.ylabel("Numero")
    plt.grid()
    plt.show()


def main():
    m = input("escriba la secuencia de numeros: ")
    lista = m.split(",")

    n = input("desea ascendente (asce) o descente (desce): ")
    if n == "asce":
        lista = asce(m, lista)
        graficar(lista, "ascendente")
    elif n == "desce":  
        lista = desce(m, lista)
        graficar(lista, "descendente")






main()
