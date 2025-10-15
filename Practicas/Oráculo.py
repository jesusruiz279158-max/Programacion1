
def calcular_elemento():

    anioN = int(input("Por favor ingrese su año de nacimiento: "))
    ultD = anioN%10

    if ultD == 0 or ultD == 1:
        return "Metal"
    elif ultD == 2 or ultD== 3:
        return "Agua"
    elif ultD == 4 or ultD == 5:
        return "Madera"
    elif ultD == 6 or ultD == 7:
        return "Fuego"
    elif ultD == 8 or ultD == 9:
        return "Tierra"


def generar_prediccion(nombre, elemento, numS):

    match numS:
        case 1:
            print(f"{nombre}, tu conexión con el elemento {elemento} te traera gran sabiduria!.¡Es un buen momento para aprender algo nuevo!")
        case 2:
            print(f"Tu conexión con el elemento {elemento} te representa {nombre}, ya que seguir asi te guiara a un buen futuro.")
        case 3:
            print(f"Asi que tu elemento es {elemento}, que suerte {nombre} ya que significa que te persigue la abundancia!")
        case 4:
            print(f"Enhorabuena {nombre} tu conexión con el elemento {elemento} te dortará con salud.")
        case _:
            print("Número de la suerte invalido. Usa 1, 2, 3 o 4.")



def iniciar_oraculo():
    while True:

        opcion = input("¿Deseas conocer tu destino?  (si/no) ").lower()

        if opcion == 'si':
            nombre = input("Por favor ingrese su nombre: ")
            elemento = calcular_elemento()
            numS = int(input("Por favor ingrese su número de la suerte (1, 2, 3, 4): "))
            generar_prediccion(nombre, elemento, numS)
        
        elif opcion == 'no':
            print("Hasta luego.")
            break

        else:
            print("Opción no valida, escriba 'Si' o 'No'.")

            
iniciar_oraculo()