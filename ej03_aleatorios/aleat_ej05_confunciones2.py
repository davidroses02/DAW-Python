"""
Muestra 50 números enteros aleatorios entre 100 y 199 (ambos incluidos) separados por espacios.
Muestra también el máximo, el mínimo, la moda, la media, la mediana y la desviación típica de esos números.

Mejora del anterior.
"""

import random
import math

# Funciones
def numeros_aleatorios(rango_inicial, rango_final, cantidad):
    """
    Genera números aleatorios y los almacena dentro de una lista enviada como parámetro.

    Parámetros:
    * rango_inicial: valor mínimo del número aleatorio a generar.
    * rango_final: valor máximo del número aleatorio a generar.
    * cantidad: cantidad de números aleatorios a generar

    Devuelve: lista donde se guardan los números aleatorios.
    """
    numeros = []
    for i in range(cantidad):
        numeros.append(random.randint(rango_inicial, rango_final))
    return numeros

def media(numeros):
    """
    Devuelve la media de la lista pasada como parámetro.
    """
    return sum(numeros)/len(numeros)

def mediana(numeros):
    """
    Devuelve la mediana de la lista pasada como parámetro.
    """
    numeros_ordenado = numeros.copy()   # creo lista nueva para no cambiar números y ordeno
    numeros_ordenado.sort()
    centro = len(numeros_ordenado) // 2
    if len(numeros_ordenado)%2 == 0:    # cantidad par, la mediana es la media de los dos centrales
        return (numeros_ordenado[centro-1]+numeros_ordenado[centro]) / 2
    else:
        return numeros_ordenado[centro]

def desvt(numeros):
    """
    Devuelve la desviación típica de la lista pasada como parámetro.
    """
    sumatorio = 0
    media_ = media(numeros)
    for n in numeros:
        sumatorio += (n-media_)**2
    return math.sqrt(sumatorio/len(numeros))

def calcula_moda(numeros, modas):
    """
    Calcula las modas de la lista pasada como parámetro.

    Parámetros:
    * numeros: lista de números.
    * modas: lista donde guardar las modas
    """

    def actualiza_frecuencia(n, frecuencias):
        """
        Busca n en la matriz de frecuencias, si lo encuentra incrementa su frecuencia.
        Si no lo encuentra crea una nueva fila.
        """
        esta_n = False
        i = 0
        while (not esta_n and i<len(frecuencias)):
            if frecuencias[i][0] == n:
                frecuencias[i][1] += 1
                esta_n = True
            i+=1
        if not esta_n:  # no está el valor n, creamos una nueva fila
            frecuencias.append([n,1])

    frecuencias = []    # matriz para guardar cada ocurrencia (columna 0) y su frecuencia (colunmna 1)
    # Cálculo de las frecuencias
    for n in numeros:
        actualiza_frecuencia(n, frecuencias)
    # Cálculo frecuencia máxima
    f_max = 0
    for f in frecuencias:
        if f[1] > f_max:
            f_max = f[1]
    # Meto las modas en el array modas
    for m in frecuencias:
        if m[1] == f_max:
            modas.append(m[0])

# Programa Principal

# Constantes
NUM = 50            # Cantidad de números aleatorios generados
RANGO_INICIAL = 100 # Rango de números aleatorios generados
RANGO_FINAL = 199

# Inicializaciones
modas = []

# Proceso
numeros = numeros_aleatorios(RANGO_INICIAL, RANGO_FINAL, NUM)
maximo_ = max(numeros)
minimo_ = min(numeros)
media_ = media(numeros)
mediana_ = mediana(numeros)
desvt_ = desvt(numeros)
calcula_moda(numeros, modas)

# Mostrar resultados
print("Números generados:", numeros)
print("Máximo:", maximo_)
print("Mínimo:", minimo_)
print("Media:", media_)
print("Mediana:", mediana_)
print("Desviación típica:", desvt_)
print("Moda: ", end="")
for moda in modas:
    print(moda, end=" ")
print()
