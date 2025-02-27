import random
#Esta funcion hace las tiradas random y determina el ganador de la tirada, devuelve 1 o 0 segun corresponda
def tiradas(nombre1, nombre2):
    opciones = {1: "Piedra", 2: "Tijera", 3: "Papel"}

    input("Presione Enter para tirar la jugada")

    jugador1 = random.randint(1, 3)
    jugador2 = random.randint(1, 3)

    print(f"{nombre1} sacó: {opciones[jugador1]}")
    print(f"{nombre2} sacó: {opciones[jugador2]}")

    if (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 == 3 and jugador2 == 2):
        print(f"{nombre1} gana esta ronda")
        return 1, 0  # Punto para el jugador 1
    elif (jugador2 == 1 and jugador1 == 3) or (jugador2 == 2 and jugador1 == 1) or (jugador2 == 3 and jugador1 == 2):
        print(f"{nombre2} gana esta ronda")
        return 0, 1  # Punto para el jugador 2
    else:
        print("¡Empate en esta ronda!")
        return 0, 0  # Empate, nadie suma puntos
    

# Pedir nombres de los jugadores
jugador1 = input("Ingrese el nombre del 1º Jugador: ")
jugador2 = input("Ingrese el nombre del 2º Jugador: ")

# Mostrar reglas
print("\nREGLAS:")
print("* Piedra vence a Tijera ")
print("* Tijera vence a Papel ")
print("* Papel vence a Piedra ")
print("* Se juegan 10 rondas")
print("* Quien gane más rondas, gana el juego")
print("* En caso de empate, se jugará una ronda extra para el desempate")

# Jugar 10 rondas
puntosJ1 = 0
puntosJ2 = 0

for i in range(1, 11):
    print(f"\n--- Tirada {i} ---")
    p1, p2 = tiradas(jugador1, jugador2)
    puntosJ1 += p1
    puntosJ2 += p2

    # Si alguien ya tiene más de 5 victorias, se puede cortar el bucle
    if puntosJ1 > 5 or puntosJ2 > 5:
        break

# En caso de empate, se juega UNA SOLA ronda extra
if puntosJ1 == puntosJ2:
    print("\n¡Empate! Se juega una ronda extra.")
    p1, p2 = tiradas(jugador1, jugador2)
    puntosJ1 += p1
    puntosJ2 += p2

# Mostrar resultado final
ganador = jugador1 if puntosJ1 > puntosJ2 else jugador2
#imprime el ganador y los puntos mas altos con la funcion max
print(f"\n¡El ganador es {ganador} con {max(puntosJ1, puntosJ2)} puntos! ")