# MIANO GASTON
# DIV 117 TM
# DESAFIO PIEDRA PAPEL O TIJERAS
from random import randint
from funciones import *

def jugar_piedra_papel_tijera()-> str:

    puntaje_jugador = 0
    puntaje_maquina = 0
    ronda_actual = 1

    mensaje = crear_mensaje_bienvenida()

    print(mensaje)

    while True:
#region Carga de datos
        print("\n----Puntaje----\n")
        print(f"Jugador: {puntaje_jugador} | CPU: {puntaje_maquina}")
        print(f"\nRonda: {ronda_actual}\n")
        print("Piedra(1) - Papel(2) - Tijera(3)")

        eleccion_jugador = input("Elija su jugada: ")

        while ( 
                (eleccion_jugador != "1" and eleccion_jugador != "2" and
                eleccion_jugador != "3")
            ):
            print("Piedra(1) - Papel(2) - Tijera(3)")
            eleccion_jugador = input("Error. Elija su jugada: ")

        eleccion_jugador = int(eleccion_jugador)

        eleccion_maquina = randint(1, 3)

        print(f"\n-Tu elección: {mostrar_elemento(eleccion_jugador)}")
        print(f"-CPU eligió: {mostrar_elemento(eleccion_maquina)}\n")
#endregion

#region ganador ronda
        ganador_ronda = verificar_ganador_ronda(eleccion_jugador,
                                                eleccion_maquina)

        if ganador_ronda == "Jugador":
            print(f"Ganaste la ronda {ronda_actual}.")
            puntaje_jugador += 1
        elif ganador_ronda == "Maquina":
            print(f"La CPU ganó la ronda {ronda_actual}.")
            puntaje_maquina += 1
        else:
            print("Empate en esta ronda.")
#endregion

        if not verificar_estado_partida(puntaje_jugador, puntaje_maquina,
                                    ronda_actual):
            break

        ronda_actual += 1
    print(f"Puntaje final:\nJugador: {puntaje_jugador}")
    print(f"CPU: {puntaje_maquina}")
    ganador_final = verificar_ganador_partida(puntaje_jugador, 
                                            puntaje_maquina, ronda_actual)

    return ganador_final

ganador = jugar_piedra_papel_tijera()

print(f"El ganador de este piedra papel o tijeras es: {ganador}")