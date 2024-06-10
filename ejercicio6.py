def decimal_a_binario(decimal):
    """Función que convierte un numero decimal a binario.
    Parámetros
        -decimal: Es un numero entero
    Salida:
        Devuelve el numero binario.
    """
    binario = []
    while decimal > 0:
        binario.append(str(n % 2))
        n //= 2
    binario.reverse()
    return ''.join(binario) 


print(decimal_a_binario(10)) 
'''
def binario_a_decimal(binario):
    """Función que convierte un binario a decimal.
    Parámetros:
        -binario: Es una cadena de 1 y 0.
    Salida:
        Devuelve el numero decimal.
    '''
'''
