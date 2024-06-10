def cuadrados_lista(numeros):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros:
        -numeros: Es una lista de números
    Salida:
        -Devuelve una lista con los cuadrados de los números de la lista.
    """
    for numero in numeros :
        resultado = numero ** 2
        return resultado 
cuadrados_lista([1, 2, 3, 4, 5])