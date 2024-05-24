import os  
import random 
import statistics 

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicializa el nombre del jugador
        self.puntaje = 0  # Inicializa el puntaje del jugador en 0
        self.tiradas = []  # Inicializa la lista de tiradas del jugador

    def tirar_dado(self):
        resultado = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6
        self.tiradas.append(resultado)  # Añade el resultado de la tirada a la lista de tiradas
        self.puntaje += resultado  # Suma el resultado al puntaje total del jugador
        return resultado  # Devuelve el resultado de la tirada

def calcular_media_varianza(tiradas):
    media = statistics.mean(tiradas)  # Calcula la media de las tiradas
    # Calcula la varianza de las tiradas, si hay menos de 2 tiradas la varianza es 0
    varianza = statistics.variance(tiradas) if len(tiradas) > 1 else 0
    return media, varianza  # Devuelve la media y la varianza

def limpiar_consola():
    # Limpia la consola dependiendo del sistema operativo
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/MacOS
        os.system('clear')

def carrera_de_dados():
    limpiar_consola()  # Limpia la consola antes de comenzar el juego
    
    # Solicita los nombres de los jugadores y crea instancias de la clase Jugador
    nombre_jugador1 = input("Ingrese el nombre del Jugador 1: ")
    nombre_jugador2 = input("Ingrese el nombre del Jugador 2: ")
    
    jugador1 = Jugador(nombre_jugador1)  # Crea el jugador 1 con el nombre ingresado
    jugador2 = Jugador(nombre_jugador2)  # Crea el jugador 2 con el nombre ingresado

    objetivo = 25  # Define el puntaje objetivo para ganar

    print("¡Bienvenidos a la Carrera de Dados con Estadísticas!")
    print(f"El primer jugador en alcanzar {objetivo} puntos o más gana la carrera.")

    turno = 1  # Inicializa el número de turnos
    # Bucle principal del juego, continúa hasta que uno de los jugadores alcance el puntaje objetivo
    while jugador1.puntaje < objetivo and jugador2.puntaje < objetivo:
        print(f"\nTurno {turno}:")
        # Cada jugador tira el dado una vez por turno
        for jugador in (jugador1, jugador2):
            resultado = jugador.tirar_dado()  # El jugador tira el dado
            print(f"{jugador.nombre} tiró un {resultado}. Puntaje total: {jugador.puntaje}")

            # Verifica si el jugador ha alcanzado o superado el puntaje objetivo
            if jugador.puntaje >= objetivo:
                print(f"\n¡{jugador.nombre} ha ganado la carrera!")
                break  # Sale del bucle si un jugador ha ganado
        turno += 1  # Incrementa el número de turnos

    # Calcula y muestra las estadísticas para ambos jugadores
    for jugador in (jugador1, jugador2):
        media, varianza = calcular_media_varianza(jugador.tiradas)  # Calcula la media y la varianza de las tiradas
        print(f"\nEstadísticas de {jugador.nombre}:")
        print(f"Tiradas: {jugador.tiradas}")
        print(f"Media de las tiradas: {media:.2f}")
        print(f"Varianza de las tiradas: {varianza:.2f}")


if __name__ == "__main__":
    carrera_de_dados()  # Llama a la función principal del juego

#Jorge, Kevin, Xavier, Allan, Carlos y Alejandro