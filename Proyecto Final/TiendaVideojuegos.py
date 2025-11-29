import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from config import TITULO,COLOR_BARRA_SUPERIOR,COLOR_MENU_LATERAL,COLOR_PANEL_PRINCIPAL
#Valores de los juegos
valor = {
    "Zelda": 90,
    "God of War": 60,
    "Halo": 30
}

#Inventario de copias
inventario = {
    "Zelda": 25,
    "God of War": 8,
    "Halo": 20
}

#Información adicional de juegos
info_juegos = {
    "Zelda": {
        "categoria": "Acción / Aventura",
        "plataformas": "Nintendo Switch",
        "descripcion": "The Legend of Zelda es una franquicia de videojuegos de acción y aventuras en la que el joven héroe Link emprende una misión para rescatar a la Princesa Zelda y salvar la tierra de Hyrule del villano Ganon."
    },
    "God of War": {
        "categoria": "Acción / Hack and Slash",
        "plataformas": "PlayStation 4 / PlayStation 5",
        "descripcion": "God Of War-(GOW) es una aclamada saga de videojuegos de acción y aventura que sigue la historia de Kratos, un guerrero espartano, en una brutal y épica búsqueda de venganza contra los dioses que lo traicionaron."
    },
    "Halo": {
        "categoria": "Shooter / Ciencia Ficción",
        "plataformas": "Xbox / Xbox Series",
        "descripcion": "Halo es una franquicia de videojuegos de ciencia ficción, principalmente del género de disparos en primera persona (FPS). La trama se centra en una guerra futurista entre la humanidad, liderada por el supersoldado Jefe Maestro, y una alianza teocrática de razas alienígenas conocida como el Covenant."
    }
}

#Ventana principal
root = tk.Tk()
root.title(TITULO)
root.geometry("1000x630")

barra_superior = tk.Frame(root,height=50, bg=COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

menu_lateral = tk.Frame(root,width=150,bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT,fill="both",expand=False)

panel_principal = tk.Frame(root,width=150, bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT, fill="both",expand=True)



#FUNCIONES DEL PROGRAMA

def mostrar_inventario():
    inv_win = tk.Toplevel()
    inv_win.title("Inventario")
    inv_win.geometry("1000x630")

    tk.Label(inv_win, text="Inventario de Juegos", font=("Arial", 14)).pack()

    texto = ""
    for juego, cant in inventario.items():
        texto += f"{juego.title()}: {cant} unidades\n"

    tk.Label(inv_win, text=texto).pack()

    tk.Label(inv_win, text="Ver gráfica por:").pack()

    tk.Button(inv_win, text="Cantidad", command=grafica_cantidad).pack(pady=5)
    tk.Button(inv_win, text="Precio", command=grafica_precio).pack(pady=5)


def grafica_cantidad():
    nombres = list(inventario.keys())
    cantidades = list(inventario.values())

    plt.figure(figsize=(8, 5))
    plt.bar(nombres, cantidades)
    plt.xlabel("Juegos")
    plt.ylabel("Cantidad")
    plt.title("Inventario de juegos por cantidad")
    plt.show()


def grafica_precio():
    nombres = list(valor.keys())
    precios = list(valor.values())

    plt.figure(figsize=(8, 5))
    plt.bar(nombres, precios)
    plt.xlabel("Juegos")
    plt.ylabel("Precio")
    plt.yticks(np.arange(0, max(precios) + 1, 10))
    plt.title("Inventario de juegos por precio")
    plt.show()


def comprar():
    comprar_win = tk.Toplevel()
    comprar_win.title("Comprar Juegos")
    comprar_win.geometry("1000x630")

    tk.Label(comprar_win, text="Selecciona un juego:", font=("Arial", 12)).pack()

    lista = tk.Listbox(comprar_win)
    lista.pack()

    for juego in inventario:
        lista.insert(tk.END, juego)

    def seleccionar_juego():
        index = lista.curselection()
        if not index:
            messagebox.showwarning("Error", "Selecciona un juego.")
            return
        juego = lista.get(index)
        mostrar_info_juego(juego, comprar_win)

    tk.Button(comprar_win, text="Ver información", command=seleccionar_juego).pack(pady=10)


def mostrar_info_juego(juego, win_padre):
    info_win = tk.Toplevel()
    info_win.title(juego.title())
    info_win.geometry("1000x630")

    tk.Label(info_win, text=f"Juego: {juego.title()}", font=("Arial", 13, "bold")).pack()

    tk.Label(info_win, text=f"Precio: {valor[juego]}").pack()
    tk.Label(info_win, text=f"Categoría: {info_juegos[juego]['categoria']}").pack()
    tk.Label(info_win, text=f"Plataformas: {info_juegos[juego]['plataformas']}").pack()

    tk.Label(info_win, text="\nDescripción:").pack()
    tk.Label(info_win, text=info_juegos[juego]['descripcion'], wraplength=350).pack()

    tk.Label(info_win, text=f"\nDisponibles: {inventario[juego]}").pack()

    def confirmar_compra():
        if inventario[juego] > 0:
            inventario[juego] -= 1
            messagebox.showinfo("Compra realizada", f"Has comprado {juego.title()}.\nQuedan {inventario[juego]} unidades.")
            info_win.destroy()
        else:
            messagebox.showerror("Sin stock", "Ya no hay copias disponibles.")

    tk.Button(info_win, text="Comprar", command=confirmar_compra).pack(pady=10)



#BOTONES PRINCIPALES
def botones_menu():
    tk.Label(root, text="Tienda de Juegos", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Ver Inventario", width=20, command=mostrar_inventario).pack(pady=10)
    tk.Button(root, text="Comprar Juegos", width=20, command=comprar).pack(pady=10)
    tk.Button(root, text="Salir", width=20, command=root.quit).pack(pady=20)

botones_menu()
root.mainloop()