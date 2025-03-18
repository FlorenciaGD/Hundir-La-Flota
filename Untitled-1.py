tablero_jugador = [[" " for i in range(10)] for j in range(10)]
tablero_computer = [[" " for i in range(10)] for j in range(10)]
tablero_disparos = [[" " for i in range(10)] for j in range(10)]

#Funcion para los tableros:

def mostrar_tablero(tablero):
    for i in tablero:
        print(i)




# Colocación barcos en el tablero del jugador

#Barcos de 1 eslora
tablero_jugador[0][0] = "B"
tablero_jugador[2][2] = "B" 
tablero_jugador[4][4] = "B"
tablero_jugador[6][6] = "B"

#Barcos de 2 esloras
tablero_jugador[1][1] = "B"
tablero_jugador[1][2] = "B" 
tablero_jugador[3][3] = "B"
tablero_jugador[3][4] = "B"
tablero_jugador[5][5] = "B"
tablero_jugador[5][6] = "B"

#Barcos de 3 esloras
tablero_jugador[7][0] = "B"
tablero_jugador[7][1] = "B" 
tablero_jugador[7][2] = "B"
tablero_jugador[8][0] = "B"
tablero_jugador[8][1] = "B"
tablero_jugador[8][2] = "B"

#Barcos de 4 esloras
tablero_jugador[9][0] = "B"
tablero_jugador[9][1] = "B" 
tablero_jugador[9][2] = "B"
tablero_jugador[9][3] = "B"

# Colocación barcos en el tablero del ordenador

#Barcos de 1 eslora
tablero_computer[0][1] = "B"
tablero_computer[1][8] = "B" 
tablero_computer[3][9] = "B"
tablero_computer[3][4] = "B"

#Barcos de 2 esloras
tablero_computer[6][0] = "B"
tablero_computer[6][1] = "B" 
tablero_computer[2][1] = "B"
tablero_computer[2][2] = "B"
tablero_computer[9][4] = "B"
tablero_computer[9][5] = "B"

#Barcos de 3 esloras
tablero_computer[7][7] = "B"
tablero_computer[7][6] = "B" 
tablero_computer[7][5] = "B"
tablero_computer[0][6] = "B"
tablero_computer[0][4] = "B"
tablero_computer[0][5] = "B"

#Barcos de 4 esloras
tablero_computer[5][3] = "B"
tablero_computer[5][4] = "B" 
tablero_computer[5][5] = "B"
tablero_computer[5][6] = "B"

def turno_jugador():
    while True:
        try:
            fila = int(input("Ingresa la fila: "))
            columna = int(input("Ingresa la columna: "))
            if 0 <= fila <= 9 and 0<= columna <= 9:
                if tablero_disparos[fila][columna] == " ":
                    if tablero_computer[fila][columna] == "B":
                        print("Yuhu! Le has dado a un barco!")
                        tablero_disparos[fila][columna] = "X"
                        tablero_computer[fila][columna] = "X"
                    else:
                        print ("Agua!")
                        tablero_disparos[fila][columna] = "O"
                        break
                else:
                    print("Mal! Ya habías disparado aquí!")
            else:
                print("Coordenadas fuera de rango")
        except ValueError:
            print("Por favor, ingresa números válidos")

import random
def turno_computer():
    while True:
        fila = random.randint(0,9)
        columna = random.randint (0,9)
        if tablero_jugador[fila][columna] == "B":
            print(f"Te han dado en ({fila}, {columna})")
            tablero_jugador[fila][columna] = "X"
            break
        elif tablero_jugador[fila][columna] == " ":
            print(f"Computer te ha disparado en ({fila}, {columna})y falló.")
            tablero_jugador[fila][columna] = "O"
            break

#Comprobar si hay ganador

def barcos_hundidos(tablero):
    for fila in tablero:
        if "B" in fila:
            return False
    return True

#Bucle del juego


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
    