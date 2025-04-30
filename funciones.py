def verificar_ganador_ronda(jugador:int , maquina: int)->str:
    """
    Recibe 2 enteros, los valores de piedra papel o tijera.
    Calcula quien gana la ronda o si hay empate.
    Retorna un string con el resultado de la ronda.
    """
    if jugador == 1:
        if maquina == 1:
            ganador = "Empate"
        elif maquina == 2:
            ganador = "Maquina"
        else:
            ganador = "Jugador"
    elif jugador == 2:
        if maquina == 1:
            ganador = "Jugador"
        elif maquina == 2:
            ganador = "Empate"
        else: 
            ganador = "Maquina"
    else:
        if maquina == 1:
            ganador = "Maquina"
        elif maquina == 2:
            ganador = "Jugador"
        else:
            ganador = "Empate"

    return ganador

def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int,
                            ronda_actual:int)-> bool:
    """
    Recibe 3 enteros, la cantidad de rondas ganadas de los 2 jugadores
    y la ronda actual.
    Calcula si la partida continua o finaliza.
    Retorna True si continua, False si finaliza.
    """
    retorno = True

    if ronda_actual <= 3:
        #Casos que cortan la partida
        if(
            (aciertos_jugador == 2 and aciertos_maquina == 0) or 
            (aciertos_jugador == 0 and aciertos_maquina == 2) or
            (aciertos_jugador + aciertos_maquina == 3 and
            ronda_actual == 3)
        ):
            retorno = False
        else:
            retorno = True
    #Caso de que empatan las 3 primeras
    else:
        if aciertos_jugador == aciertos_maquina:
            retorno = True
        else:
            retorno = False
    
    return retorno

def verificar_ganador_partida(aciertos_jugador: int,
                            aciertos_maquina: int, ronda_actual: int)-> str|None:
    """
    Recibe 3 enteros, la cantidad de rondas ganadas de los 2 jugadores
    y la ronda actual.
    Calcula el ganador y lo retorna en formato string.
    """
    ganador = None
    
    if verificar_estado_partida(aciertos_jugador, aciertos_maquina,
                                ronda_actual) == False:
        if aciertos_jugador > aciertos_maquina:
            ganador = "Jugador"
        else:
            ganador = "Maquina"


    return ganador
    
def mostrar_elemento(eleccion: int)-> str:
    """
    Recibe un entero con el número de elección.
    Retorna un string con Piedra, Papel o Tijera.
    """
    if eleccion == 1:
        jugada = "Piedra"
    elif eleccion == 2:
        jugada = "Papel"
    else:
        jugada = "Tijera"

    return jugada

def crear_mensaje_bienvenida()->str:

    mensaje = ""
    mensaje += "\nBienvenidos a Piedra, papel o tijera!\n"
    mensaje += "Se enfrentará a la CPU al mejor de 3 rondas.\n"
    mensaje += "Las reglas son sencillas:\n- Cada jugador hara su elección "
    mensaje += "entre Piedra(1), Papel(2), o Tijeras(3).\n- La partida es "
    mensaje += "al mejor de 3. En caso de que un jugador gane 2 veces "
    mensaje += "seguidas, la partida finalizara automáticamente.\nSi "
    mensaje += "termina en empate luego de 3 rondas, el juego "
    mensaje += "sigue hasta que uno gane."
    
    return mensaje