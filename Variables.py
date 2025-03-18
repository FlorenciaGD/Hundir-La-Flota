tablero_jugador = [[" " for i in range(10)] for j in range(10)]
tablero_computer = [[" " for i in range(10)] for j in range(10)]
tablero_disparos = [[" " for i in range(10)] for j in range(10)]


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