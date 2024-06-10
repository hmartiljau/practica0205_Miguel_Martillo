def calcular_media(numeros):
    """Función que calcula la media de una muestra de números.
    Parámetros:
        -numeros: Es una lista de números
    Salida:
        -Devuelve la media de los números. 
    """
    suma = sum(numeros)
    cantidad = len(numeros)
    media= suma/cantidad
    return media

calcular_media([1, 2, 3, 4, 5])