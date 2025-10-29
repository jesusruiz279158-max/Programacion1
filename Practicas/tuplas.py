#TIENDA DE VIDEOJUEGOS

info_tienda = ("Game Stop!", "2004")   #Tupla

inventario = {
    "mario world":{'precio':50,'stock':10},
    "minecraft":{'precio':40,'stock':15},
    "gta 6":{'precio':100,'stock':3},
}

print("============ ¡Bienvenido a Game Stop!============")
#print(f"\nEl precio del segundo juego es: {inventario['minecraft']['precio']}\n")

print("Los juegos en existencia son: \n")

for juegos in inventario:
    print(f"{juegos}    ${inventario[juegos]['precio']}  Unidades: {inventario[juegos]['stock']}".capitalize())

while True:
    
    opcion = input("\nDesea comprar algun juego? (si/no): \n").lower()

    if opcion == 'si':
        juegoC = input("Ingrese el nombre del juego que desee comprar: \n").lower()

        if juegoC in inventario:
            print("==========================================")
            print(f"Usted ha comprado el juego '{juegoC}.'")
            inventario[juegoC]["stock"] -= 1
            print(f"Las copias disponibles de '{juegoC}' ahora son: {inventario[juegoC]['stock']}")
            print("==========================================")
    
    elif opcion == 'no':
        print("Siempre será bienvenido..")
        break
    else:
        print("Por favor ingrese una respuesta válida..")
