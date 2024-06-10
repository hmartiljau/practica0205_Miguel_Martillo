pi = 3.141592653589793
def area_circulo(radio):
    """Función que calcula el area de un círculo.
    Parámetros:
        -radio: Es el radio del círculo.
    Salida:
        -Devuelve el área del círculo . 
    """
    circulo = pi * radio ** 2
    return round(circulo,2)

def volumen_cilindro(radio, altura):
    """Función que calcula el volumen de un cilindro.
    Parámetros
        -radio: Es el radio de la base del cilindro.
        -altura: Es la altura del cilindro.
    Salida:
        -Devuelve el volumen del clindro.
    """
    volumen = area_circulo(radio) * altura
    return round(volumen,2)

area_circulo(3)
volumen_cilindro(3, 5)