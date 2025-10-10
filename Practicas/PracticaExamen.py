print("========================EXAMEN PROGRAMACIÓN========================\n")

print("Por favor ingrese las respuestas en mayusculas. ej: A, B, C, D.\n")

respuestas_correctas = 0

#Pregunta 1

opcion1 = "A). Bucle 'para'", "B). Sentencia condicional 'Si'", "C). Bucle 'repetir'", "D). Bucle 'mientras'"
print("1. ¿Cuál estructura de control es más adecuada para iterar sobre una secuencia de elementos?")
r01 = input(opcion1)

if r01 == 'A': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r01 in ('B', 'C', 'D'):
    print("La respuesta es incorrecta\n") 
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 2

opcion2 = "A). Un conjunto de instrucciones escritas en código binario.", "B). El código fuente de un programa de computadora.", "C). El conjunto de pasos ordenados y finitos para resolver un problema.", "D). Un lenguaje de programación de alto nivel."
print("2. ¿Qué es un algoritmo?")
r02 = input(opcion2)

if r02 == 'C': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r02 in ('B', 'A', 'D'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 3

opcion3 = "A). Símbolos lógicos y matemáticos", "B). Pseudocódigo", "C). Instrucciones en inglés abreviado", "D). Ceros y unos."
print("3. El lenguaje máquina está compuesto por: ")
r03 = input(opcion3)

if r03 == 'D': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r03 in ('B', 'A', 'C'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 4

opcion4 = "A). Sistema de entrada/Salida", "B). CPU", "C). Tarjeta Gráfica", "D). Memoria principal"
print("4. ¿Cuál de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neumann?")
r04 = input(opcion4)

if r04 == 'C': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r04 in ('B', 'A', 'D'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 5

opcion5 = "A). Ser el más antiguo de los lenguajes.", "B). Ser el más rápido en tiempo de ejecución.", "C). Estar orientado a la interacción con el hardware.", "D). Ser independiente de la arquitectura de la computadora."
print("5. Un lenguaje de programación de alto nivel se caracteriza por:")
r05 = input(opcion5)

if r05 == 'D': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r05 in ('B', 'A', 'C'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 6

opcion6 = "A). Bajo", "B). Medio-Bajo", "C). Medio", "D). Alto"
print("6. El lenguaje Java es considerado un lenguaje de nivel...")
r06 = input(opcion6)

if r06 == 'D': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r06 in ('B', 'A', 'C'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 7

opcion7 = "A). Una colección de algoritmos.", "B). El sistema operativo de una computadora.", "C). La secuencia de instrucciones y datos que la computadora ejecuta.", "D). El diseño del hardware interno de la computadora."
print("7. Un programa de computadora es esencialmente:")
r07 = input(opcion7)

if r07 == 'C': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r07 in ('B', 'A', 'D'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 8

opcion8 = "A). Sentencia condicional 'Si'", "B). Repetitiva 'para'", "C). Secuencial", "D). Repetitiva 'mientras'"
print("8. En pseudocódigo, ¿qué estructura de control se utiliza para ejecutar un bloque de código solo si se cumple una condición específica?")
r08 = input(opcion8)

if r08 == 'A': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r08 in ('B', 'D', 'C'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 9

opcion9 = "A). Traducir automáticamente código de alto nivel a lenguaje máquina.", "B). Asegurar la sintaxis correcta del código antes de que sea compilado.", "C). Clasificar y describir la lógica de un algoritmo de forma legible para los humanos.", "D). Ser un reemplazo directo del lenguaje de programación Python."
print("9. El propósito principal del pseudocódigo es:")
r09 = input(opcion9)

if r09 == 'C': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r09 in ('B', 'A', 'D'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

#Pregunta 10

opcion10 = "A). El bucle 'mientras' puede no ejecutarse, mientras que el 'repetir' se ejecuta al menos una vez.", "B). El bucle 'mientras' solo acepta números y el 'repetir' solo acepta cadenas.", "C). El bucle 'mientras' es más rápido que el 'repetir'.", "D). El bucle 'repetir' solo usa números, mientras que el 'mientras' puede usar cualquier condición."
print("10. ¿Cuál es la principal diferencia entre un bucle 'mientras' (while) y un bucle 'repetir' (do-while)?")
r10 = input(opcion10)

if r10 == 'A': 
    print("La respuesta es correcta\n")
    respuestas_correctas += 1
elif r10 in ('B', 'D', 'C'):
    print("La respuesta es incorrecta\n")
else:
    print("Por favor ingrese una respuesta válida\n")

print("=======================================================================")
print("La cantidad de respuestas correctas son: " , respuestas_correctas)
if respuestas_correctas >= 6:
    print ("Usted ha aprobado el examen")
else:
    print("Usted ha reprobado el examen")
print("=======================================================================")