#!/usr/bin/env python3

import socket
import time
import pickle
#print("Indique la ip del servidor")
HOST = "127.0.0.1"  # input()  # El hostname o la IP del servidor "127.0.0.1"
#print("Indique el puerto que utiliza el servidor")
PORT = 12345  # int(input())  # El puerto que usa el servidor 12345
buffer_size = 1024

tablero = []
jugador1Activo = True
# contador de pares
scoreJugador1 = 0
scoreJugador2 = 0
def tableroDesplegar(enJuego):
    # ciclo por linea
    for linea in tablero:

        # ciclo por columnas
        for palabra in linea:
            if palabra == "*J1*" or palabra == "*J2*":
                print(palabra, end="  ")
            else:
                if enJuego:
                    print("------", end="  ")
                else:
                    print(palabra, end="  ")

        # cambio de linea
        print()

    # deja una linea
    print()

# Funcion que verifica si es par
def esParJ1(J1carta1ren, J1carta1col, J1carta2ren, J1carta2col):
    # variable para resultado
    bEsPar = False

    # compara
    if (tablero[J1carta1ren][J1carta1col] == tablero[J1carta2ren][J1carta2col]):
        # Desplega mensaje
        print("hiciste un par")

        # coloca a que jugador pertenece el par realizado
        # coloca jugador1
        tablero[J1carta1ren][J1carta1col] = "*J1*"
        tablero[J1carta2ren][J1carta2col] = "*J1*"

        # Variable de resultado
        bEsPar = True
    else:
        # Despliega mensaje de error
        print("Fallaste")

    # Pausa para continuar
    input("Presione ester para continuar...\n")
    return bEsPar

# funcion para obtener  una carta seleccionada
def cartaSeleccionadaValida(ren, col):
    valida = True
    if (tablero[ren][col] == "*J1*" or tablero[ren][col] == "*J2*"):
        valida = False

    else:
        valida = True
    # retorna la carta seleccionada
    return valida

def cartaSeleccionada(ren,col):
    return (tablero[ren][col])

print("Elige la dificultad el juego")
print("1 : Principiante")
print("2 : Avanzado")
dificultad = input()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    print("Enviando mensaje...")
    TCPClientSocket.send(dificultad.encode("utf-8"))
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    if(data.decode() == "4"):
        print("Principiante")
        ordenTablero = 4
    else:
        print("Avanzado")
        ordenTablero = 6
    
    #print("Recibido,", data.decode(), " de", TCPClientSocket.getpeername())
    tablero = pickle.loads(TCPClientSocket.recv(buffer_size))

    tableroDesplegar(True)
    print("Cartas a jugar")
    print()

    tableroDesplegar(False)
