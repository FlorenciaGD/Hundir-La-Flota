
## README

## Estructura de archivos principales

* HundirLaFlota.py: programa principal
* Funciones.py: todas las funciones necesarias
* Variables.py: todas las variables necesarias
* Archivos Notebooks: utilizados para pruebas

## Estructura códigos

1. Se crean tableros para el jugador, el ordenador y los disparos, para ello utilizo listas de 10 filas y 10 columnas:

    - "tablero_jugador" posiciona los barcos del jugador 
    - "tablero_computer" posiciona los barcos del ordenador
    - "tablero disparos" Aquí se verán los disparos del jugador.
    - Función "mostrar_tablero" con el objetivo de visualizar el tablero con los disparos


2. Posiciones fijas de los barcos
3. Se crean funciones para los turnos de disparos del jugador y del ordenador con las funciones
4. Bucles en el cual se muestra el tablero del jugador y el de disparos y va alternando entre el turno del jugador y del ordenador
5. El juego termina cuando todos los barcos de un jugador son hundidos


    * En el bucle añado try y except por si el jugador ingresa una coordenada que no es un numero, en tal caso responderá con un "Por favor, ingresa coordenadas válidas". Try ejecuta un código que podría darme error. Except ValueError captura el error cuando el jugador introduce un valor que no es un número.