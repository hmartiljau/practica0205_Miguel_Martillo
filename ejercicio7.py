def contar_palabras(texto):

    '''Función que recibe un fragmento de texto y nos indica la frecuencia 
    de las palabras que aparece

    Parámetros:
        texto: El texto del cual se quieren contar las palabras.

    Salida:
    DEvuelve un diccionario con las palabras y su frecuencia.'''

    frecuencias = {}
    texto = texto.lower()
    palabras = texto.split()
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    

    print(frecuencias) 


texto = "Hola hola mundo mundo mundo que que tal"
contar_palabras(texto)