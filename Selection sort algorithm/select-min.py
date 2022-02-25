# Its important to save references to values.

from array import array


def findMin(arrayObject):
    min_value_array = arrayObject[0] # Referencia al primer elemento del array que es usado despues para comparar.
    min_value = 0 # Referencia al valor minimo que puede haber en un array, est valor ira variando con los valores minimos
                    # que se supone hay dentro del array

    for i in range(1, len(arrayObject)):
        if arrayObject[i] < min_value_array: # Si un valor encontrado en el array es menor a la primera referencia que antes guarde:
            min_value_array = arrayObject[i] # ahora la referencia al primer elemento del array es el valor que se encontro mas pequeño al que se guardo.
            min_value = i # Y devuelves el valor minimo encontrado dentro de ese array.
    return min_value

def selectionSort(arrayObject):
    newArraySorted = [] # Nueva lista que guardara los elementos ordenados.
    for i in range(len(arrayObject)):
        min_value = findMin(arrayObject) # el minimo valor dentro del array pasado por argumento
        newArraySorted.append(arrayObject.pop(min_value)) # añades ese valor al nuevo array ordenado, retirandolo del dada por argumento
    return newArraySorted                                   # Lo que estas añadiendo es el valor minimo encontrado en el array dado, la funcion de 'findMin'


if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))