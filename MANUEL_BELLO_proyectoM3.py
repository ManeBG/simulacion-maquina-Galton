# Simulacion de la maquina de Galton.
"""
LAS CARACTERISTICAS DEL PROGRAMA:
1.- Sera la simulacion de una maquina de Galton de 3000 canicas.
2.- En total tendras 12 nivele de obstaculos - se debera decidir si va a acaer a un lasdo o al otro lado 12 veses
3.- El resultado final sera un histograma que represente la cantidad de canicas en cada contenedor, como el siguiente -No olvides colocar nombre a los ejes y un titulo al grafico.
4.- Se debera emplear dos funciones una para calcular el resultado de las canicas y la segunda para la gratificacion del histograma.
"""
###################################################################################################################

import random
import matplotlib.pyplot as plt

#Funcion donde creamos el calculo pa la simulacion del recorrido de las 3000 canicas.
def simular_canicas(num_canicas, num_niveles):
    contenedores = [0] * (num_niveles + 1)  # Inicializamos los contenedores en 0

    for _ in range(num_canicas):
        posicion = 0  # Iniciamos en el nivel más alto
        for _ in range(num_niveles):
            if random.random() < 0.5:  # Probabilidad de caer a la izquierda o derecha
                posicion += 1
        contenedores[posicion] += 1  # Incrementamos el contenedor correspondiente

    return contenedores


# Funcion que gratificara el histograma
def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores, color='blue')
    plt.title('Simulación de la Máquina de Galton')
    plt.xlabel('Contenedores')
    plt.ylabel('Número de Canicas')
    plt.show()


# Parte dnde se ejecuta la simulacion y graficaran resultados
num_canicas = 3000
num_niveles = 12
contenedores = simular_canicas(num_canicas, num_niveles)
graficar_histograma(contenedores)