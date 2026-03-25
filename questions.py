import random
import string

categorias = {
            "tipo" : ["cadena", "entero", "lista"],
            "herramienta":["python", "variable"], 
            "estructura":["programa", "funcion", "bucle"]
}
# words = [
#   "python",
#   "programa",
#   "variable",
#   "funcion",
#   "bucle",
#   "cadena",
#   "entero",
#   "lista",
# ]

# word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")

tema = input("""Seleccione una categoría para jugar:
             -tipo
             -herramienta
             -estructura
             Su elección: """).lower().strip()
while tema not in categorias:                               # Mod 3
    print()
    tema = input("""Categoria invalida.
Seleccione una categoría para jugar:
             -tipo
             -herramienta
             -estructura
             Su elección: """)
    
words = random.sample(categorias[tema], len(categorias[tema]))     

print()
points = 0
total_points = 0

for word in words:

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        print()

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")

            points +=6
            print(f"Obtuviste {points} puntos en esta ronda")                 # Mod 2

            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        print()

        letter = input("Ingresá una letra: ").lower()
        if len(letter) != 1 or letter not in string.ascii_lowercase:
            print("Entrada no válida")                          # Mod 1

        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")

            points -= 1                                         # Mod 2

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")

        print("Ha obtenido 0 puntos en esta ronda")                           # Mod 2
        points = 0

    total_points += points
    points = 0
    attempts = 6
    guessed = []
    print()
    if word != words[-1]:
        print("Ahora otra palabra: ")

print(f"Terminó el juego con {total_points} puntos")