import random

palabras = (
    "libro",
    "playa",
    "noche",
    "manos",
    "verde"
)

while True:
    palabra = palabras[random.randint(0,len(palabras)-1)] #abajo
    wordle = list(palabra) #"a", "b", "a", "j", "o"
    print("""\033[1;35;43m
=======================================[WORDLE]========================================
    Bienvenido, ya he elegido la palabra secreta. TIenes 5 intentos para adivinarlo.   
=======================================================================================
\033[0;35;43m""")
    
    for i in range (5):
        intento = input("Ingrese una palabra de 5 letras sin acento: ").lower()[:5]
        indice = 0
        resultado = ""
        correctas = 0
        for letra in intento:
            if letra == wordle[indice]:
                correctas += 1
                resultado += "\033[1;32m"+letra+"[0;35m"
            elif letra in wordle:
                resultado += "\033[1;33m"+letra+"[0;35m"
            else:
                resultado += "\033[1;31m"+letra+"[0;35m"
            indice += 1
        print(resultado)
        if correctas == 5:
            break
    
    if correctas == 5:
        print(f"Felicidades la plabra era \033[1;32m{palabra}\033[0;30m has acertado.")
    else:
        print(f"Lo siento has fallado. La palabra era: \033[1;32m{palabra}\033[0;30m")

    opcion = input("Deseas jugar otra ronda? (Si/No)".lower())
    if opcion == "no":
        break

    break