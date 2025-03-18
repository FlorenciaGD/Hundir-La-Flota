
tablero_jugador = [[" " for i in range(10)] for j in range(10)]
tablero_computer = [[" " for i in range(10)] for j in range(10)]
tablero_disparos = [[" " for i in range(10)] for j in range(10)]

def mostrar_tablero(tablero):
    for i in tablero:
        print(i)

def turno_jugador():
    while True:
       # try:
            fila = int(input("Ingresa la fila: "))
            columna = int(input("Ingresa la columna: "))
            if 0 <= fila <= 9 and 0<= columna <= 9:
                if tablero_disparos[fila][columna] == " ":
                    if tablero_computer[fila][columna] == "B":
                        print("Yuhu! Le has dado a un barco!")
                        tablero_disparos[fila][columna] = "X"
                        tablero_computer[fila][columna] = "X"
                        break
                    else:
                        print ("Agua!")
                        tablero_disparos[fila][columna] = "O"
                        break
                else:
                    print("Mal! Ya habías disparado aquí!")
            else:
                print("Coordenadas fuera de rango")
        #kexcept ValueError:
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
    print("Has ganado! Has hundido todos los barcos! :)")
    return True
