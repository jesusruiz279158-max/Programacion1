README.txt

Sistema de Inventario de Videojuegos

Descripción

Este proyecto es un sistema de inventario creado en Python que permite
administrar un catálogo de videojuegos.
El sistema funciona mediante un menú interactivo que permite:

-   Ver el inventario y generar un gráfico de existencias.
-   Agregar nuevos juegos.
-   Eliminar juegos registrados.
-   Buscar juegos por nombre.
-   Guardar los datos en un archivo CSV.

El catálogo se guarda automáticamente y puede ser modificado durante la
ejecución del programa. También se genera un gráfico de barras
(inventario_barras.png) con las existencias de cada juego.

Instrucciones de Ejecución

1.  Asegúrate de tener los archivos:
    -   main.py
    -   util.py
    -   graficos_reportes.py
2.  Instala las dependencias necesarias ejecutando:

pip install pandas matplotlib colorama

3.  Ejecuta el programa desde la terminal usando:

python main.py

4.  El menú mostrará las opciones disponibles:

5.  Ver Inventario y Estadísticas

6.  Agregar Nuevo Juego

7.  Eliminar Juego

8.  Buscar Juego por Nombre

9.  Salir

Ejemplo de Ejecución

Inicio del programa: — SISTEMA DE INVENTARIO DE VIDEOJUEGOS — 1. Ver
Inventario y Estadísticas 2. Agregar Nuevo Juego 3. Eliminar Juego 4.
Buscar Juego por Nombre 5. Salir Seleccione una opción (1-5):

Al ver el inventario: — INVENTARIO Y ESTADÍSTICAS — Gráfico de
inventario generado en ‘inventario_barras.png’.

Notas

-   Si no existe un archivo catalogo_juegos.csv, se genera uno
    automáticamente con un catálogo inicial.
-   Al seleccionar la opción 5, los cambios se guardan y el programa se
    cierra.
-   La gráfica de inventario se guarda automáticamente sin necesidad de
    abrirla.

