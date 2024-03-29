#Ejercicio 5: Escribir una función para devolver la posición que ocupa un valor pasado como parámetro, utilizando búsqueda secuencial en una lista desordenada.
#La función debe devolver -1 si el elemento no se encuentra en la lista.

#Funcion generarlista:
def genLista():
    #creamos lista vacia
    lista = []
    #pedimos numero
    nro = int(input("Ingrese un numero (-1 para finalizar): "))
    while nro != -1:
        #procesar dato
        lista.append(nro)
        nro = int(input("Ingrese un numero(-1 para finalizar): "))
    return lista
#Funcion busqueda secuencial:
def busSecuencial(lista,nro):
    i = 0
    #busco en la lista y si el orden no encuentra el numero aumenta el contador
    while i < len(lista) and lista[i] != nro:
        i += 1
    
    #si el contador es igual a la longitud de lista no se encontró
    if i == len(lista):
        encontrado = -1
    else:
        #caso contrario, se encontro el lugar y se devuelve el lugar en la lista
        encontrado = i
    return encontrado

#Funciín busqueda secuencial, todas las posiciones en la que se encuentra
def busSecuencialTodas(lista, nro):
    '''Devuelve una lista con todas las posiciones en la que se encuentra el nro.
    Devuelve la lista vacía si no se encuentra.'''
    posiciones=[]
    i = 0
    #busco en la lista y si el orden no encuentra el numero aumenta el contador
    while i < len(lista):
        if lista[i] == nro:
            posiciones.append(i)
        i += 1
    return posiciones

#Programa principal:
numeros = genLista()
print(numeros)
n = int(input("Ingrese el numero a buscar en la lista: "))
#En estos casos es recomendable que llames a la función y recibas la información en una variable, sino se ejecuta dos veces.
#una para evaliar si esta y otra para informar la posición.
if busSecuencial(numeros,n) == -1:
    print("El numero no se encontró en la lista ")
else:
    print("La primer posición en la que se encuentra en numero",n,"es: ", busSecuencial(numeros,n))

listaPos = busSecuencialTodas(numeros,n)
if  len(listaPos)==0:
    print("El numero no se encontró en la lista ")
else:
    print("El numero",n,"se encuentra en las posicioes: ", listaPos)
