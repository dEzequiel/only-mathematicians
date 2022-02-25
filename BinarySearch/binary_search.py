# En busqueda binaria te vas al medio de la coleccion de elementos. Desde ahi empiezas a buscar. Solo buscas un elemento

def binarySearch(collectionElements, searchedElement):

    left = 0 # Guardas la referencia de la izquierda
    right = len(collectionElements) - 1 # Guardas la referencia de la derecha

    # Guardas tales referencias para poder calcular el medio

    while left <= right:
        mid = (left + right) // 2   # EL medio de la colleccion es el minimo valor de posicion, 0, sumado con el maximo valor de posicion dividido entre 2.
        estimatedValue = collectionElements[mid]    # La division te dara el numero de posicion que se encuentra en medio de la coleccion, te situas en el medio.

        if estimatedValue == searchedElement:    # Si el valor de la posicion es igual al que buscas, wuala! lo encontraste
            return mid

        if estimatedValue > searchedElement:    # Si el valor de la posicion es mayor al que buscas, estas situado muy en el right, muevete al left con -1
            right = mid - 1
        else:                               # Si el valor de la posicion es menor al que buscas, estas situado muy en el left, muevete al right con +1
            left = mid + 1

    return None # Nada si  no lo encuentras
