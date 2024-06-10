def factorial_iterativo(numero):
    
    '''Función que calcula el factorial de un número de manera iterativa.

    Parámetros:
        -numero: El número del cual se quiere calcular el factorial

    Salida:
        -Devuelve el factorial del número dado.'''
    
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

factorial_iterativo(5)

def factorial_recursivo(numero):
    '''Función que calcula el factorial de un número de manera recursiva.

    Parámetros:
        -numero: El número del cual se quiere calcular el factorial

    Salida:
        -Devuelve el factorial del número dado.'''

    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

factorial_recursivo(5)