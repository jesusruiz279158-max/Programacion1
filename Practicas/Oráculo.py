
def calcular_elemento(anioAc, anioN):

    anioAc = int(2025)
    anioN = int(input("Por favor ingrese su año de nacimiento: "))
    ultD = anioN%10
    if ultD == 0 | 1 :
        return "Metal"
    elif ultD == 2 | 3 :
        return "Agua"
    elif ultD == 4 | 5 :
        return "Madera"
    elif ultD == 6 | 7 :
        return "Fuego"
    elif ultD == 8 | 9 :
        return "Tierra"

    elemento = calcular_elemento(anioAc, anioN)



def generar_prediccion(nombre, elemento, numS):

    nombre = input("Por favor ingrese su nombre: ")
    numS = int(input("Por favor ingrese su número de la suerte (1, 2, 3, 4): "))

    match numS:
        case 1:
            f"{nombre}, tu conexión con el elemento {elemento} te traera gran sabiduria!.¡Es un buen momento para aprender algo nuevo!"
        case 2:
            f"Tu conexión con el elemento {elemento} te representa {nombre}, ya que seguir asi te guiara a un buen futuro."
        case 3:
            f"Asi que tu elemento es {elemento}, que suerte {nombre} ya que significa que te persigue la abundancia!"
        case 4:
            f"Enhorabuena {nombre} tu conexión con el elemento {elemento} te dortará con salud."



def iniciar_oraculo():
    while True:

        opcion = input("¿Deseas conocer tu destino?  (si/no) ").lower()

        if opcion == 'si':
            
            calcular_elemento()
            generar_prediccion()
        
        elif opcion == 'no':
            print("Hasta luego.")
            break
iniciar_oraculo()