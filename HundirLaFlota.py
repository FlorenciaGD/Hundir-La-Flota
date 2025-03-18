import os
import time
from Variables import*
from Funciones import*


print("Bienvenido a Hundir La Flota")
while True:
    print("Tu tablero:")
    mostrar_tablero(tablero_jugador)
    print("Tablero de disparos")
    mostrar_tablero(tablero_disparos)

    print("Tu turno:")
    turno_jugador()
    if barcos_hundidos(tablero_computer):
        print("Has ganado!")
        break
    print("Turno ordenador")
    turno_computer()
    if barcos_hundidos(tablero_jugador):
        print("El ordenador te ha dado una paliza! Game over!")
        break
