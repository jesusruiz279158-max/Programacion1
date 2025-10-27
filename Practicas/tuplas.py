#TIENDA DE VIDEOJUEGOS

info_tienda = ("Game Stop!", "2004")   #Tupla

inventario = {
    "Mario World":{'precio':50,'stock':10},
    "Minecraft":{'precio':40,'stock':15},
    "GTA 6":{'precio':100,'stock':3},
}
print(f"El precio del segundo juego es: {inventario['Minecraft']['precio']}")

print(f"Los juegos disponibles son {inventario}")
input("Desea comprar algun juego?:   (si/no)")

