import random as r

opciones = ['P','A','T']

#Motor del juego
def piedraPapelOTijeras():
    puntosUsuario = 0
    puntosOrdenador = 0
    numeroPartidas = 0
    cantidadPartidas = int(input("Bienvenido al juego de piedra, papel o tijera.\nIngrese la cantidad de partidas a jugar: "))
    
    while True:
        numeroPartidas += 1
        eleccionUsuario = obtenerEleccionUsuario()
        eleccionOrdenador = obtenerEleccionOrdenador()
        ganador = obtenerGanador(eleccionUsuario, eleccionOrdenador)
        if ganador is None:
            print("En esta parida hubo un empate")
        elif ganador == "Usuario":
            puntosUsuario += 1
            print("En esta partida el ganador fue el usuario")
        else:
            puntosOrdenador += 1
            print("En esta partida el ganador fue el ordenador")
        
        if (numeroPartidas == cantidadPartidas):
            print(f"\nEl numero de partidas jugadas fueron: {numeroPartidas}")
            verPuntos(puntosUsuario, puntosOrdenador)
            break
    
#Función para consultar la entrada del jugador:        
def obtenerEleccionUsuario():
    while True:
        eleccionUsuario = input("Ingrese su eleccion: Piedra (P), Papel (A), Tijera (T):").upper()
        #Verificamos si la opcion ingresada por el usuario esta la lista donde se encuentran las 3 opciones del juego.
        #Si se encuentra, la retornamos, caso contrario, solicitamos otra vez.
        if (eleccionUsuario in opciones):
            return eleccionUsuario
        else:
            print("Opcion invalida, por favor elige: Piedra (P), Papel (A), Tijera (T)")
            
#Función para obtener la opción elegida por el ordenador:
def obtenerEleccionOrdenador():
    return r.choice(opciones)

#Funcion para comparar las opciones elegidas entre el usuario y el ordenador, para luego determinar el ganador por partida.
def obtenerGanador(eleccionUsuario, eleccionOrdenador):

    if (eleccionUsuario == eleccionOrdenador):
        print(f"Ordenador elegio la opcion: {eleccionOrdenador}. La tuya {eleccionUsuario}")
        print("En esta partida el resultado fue un empate")
        return None
    elif ((eleccionUsuario == opciones[0] and eleccionOrdenador == opciones[2]) or (eleccionUsuario == opciones[1] and eleccionOrdenador == opciones[0]) or (eleccionUsuario == opciones[2] and eleccionOrdenador == opciones[1])):
        print(f"Ordenador eligio la opcion: {eleccionOrdenador}. La tuya {eleccionUsuario}")
        return "Usuario"
    else:
        print(f"Ordenador eligio la opcion: {eleccionOrdenador}. La tuya {eleccionUsuario}")
        return "Ordenador"

def verPuntos(usuarioPuntos, ordenadorPuntos):
    
    if (usuarioPuntos == ordenadorPuntos):
        print(f"\nRESULTADO FINAL:\nPuntos Usuario: {usuarioPuntos}\nPuntos Ordenador: {ordenadorPuntos}")
        print("EMPATE!!")
    elif (usuarioPuntos > ordenadorPuntos):
        print(f"\nRESULTADO FINAL:\nPuntos Usuario: {usuarioPuntos}\nPuntos Ordenador: {ordenadorPuntos}")
        print("Ganaste!! El piedra papel o tijera!!")
    else:
        print(f"\nRESULTADO FINAL:\nPuntos Usuario: {usuarioPuntos}\nPuntos Ordenador: {ordenadorPuntos}")
        print("Perdiste :( !! El piedra papel o tijera!!")
 
def main():
    piedraPapelOTijeras()
main()        

    


    
        
     
