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
tema = input("""Seleccione una categoría para jugar
             -tipo
             -herramienta
             -estructura
             Su elección: """)
word = random.choice(categorias[tema])                      # Mod 3

print()
points = 0

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
        print(f"Obtuviste {points} puntos")                 # Mod 2

        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    print()

    letter = input("Ingresá una letra: ").lower()

    if letter not in string.ascii_lowercase:
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

    print("Ha obtenido 0 puntos")                           # Mod 2