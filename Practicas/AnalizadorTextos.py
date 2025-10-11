print("\n---------------Analizador De Texto en Python---------------")

#Pedimos un texto para analizar:
texto = input("Por favor introduzca un texto largo para analizar: ").lower()

letras_buscadas = []

#Ciclo for para verificar que si sean 3 letras:
for i in range(3):
    #Solicitar las letras
    letra = input(f"Ingresa la letra número {i+1}: ").lower()
    # Aunque el reto no lo exige, es una buena práctica asegurar que sea una sola letra
    letras_buscadas.append(letra[0]) # Solo tomo el primer carácter por si acaso
    
print("\n---Analisis del Texto---")

 # --- Parte 1: Conteo de letras ---

#Se almacenan los resultados del conteo
conteo_letras = {}
print("\n1. Frecuencia de las letras:")
#Iteramos sobre la lista de letras que el usuario ingresó
for letra in letras_buscadas:
    #Se utiliza.count()para contar las apariciones de las letras en el texto
    cantidad = texto.count(letra)
    conteo_letras[letra] = cantidad
    print(f"   La letra '{letra}' aparece {cantidad} veces.")

# --- Parte 2: Cantidad total de palabras ---

# Dividimos el texto en una lista de palabras usando .split()
# Separa el texto en palabras ej: "Hola mundo", .split() en ["Hola", "mundo"]
palabras = texto.split()

#se utiliza .len() para contar la cantidad de palabras separadas en el texto con .spilt()
#ej: "Hola mundo", .split() en ["Hola", "mundo"] ---> en este caso .len() contara 2 palabras por Hola y mundo
cantidad_palabras = len(palabras)
print(f"\n2. Cantidad total de palabras: {cantidad_palabras}")

# --- Parte 3: Primera y última letra del texto ---

# Usamos [0] para elegir la primera letra y [-1] para la última
# Aseguramos que el texto no esté vacío
if texto:
    primera_letra = texto[0]
    ultima_letra = texto[-1]
    print(f"\n3. Primera letra del texto: '{primera_letra}'")
    print(f"4. Última letra del texto: '{ultima_letra}'")
else:
    print("\n3. y 4. El texto ingresado está vacío, no se puede obtener la primera o última letra.")

# --- Parte 4: Texto con palabras en orden inverso ---

# 1. Invertimos la lista de palabras

#Se utiliza Slicing (rebanado) con la sintaxis [inicio:fin:paso].
#palabras[::-1]: Se dejan el inicio y el fin vacíos para seleccionar toda la lista. 
#Un paso negativo (-1) le indica a Python que recorra la secuencia hacia atrás.

palabras_invertidas = palabras[::-1]
 # 2. Unimos la lista invertida con .join() de nuevo en un string con espacios entre cada palabra
texto_invertido = " ".join(palabras_invertidas)
print(f"\n5. Texto con palabras en orden inverso:\n   -> {texto_invertido}")

# --- Parte 5: Búsqueda de la palabra "python" ---

# Usamos el operador 'in' para verificar si un string contiene otro substring
print("\nIndicador si la palabra 'python' esta en el texto: ")
if "python" in texto:
   respuesta_python = "Si, está la palabra python en el texto."
   print("\n", respuesta_python)
else:
    respuesta_python = "No está la palabra python en el texto."
    print("\n",respuesta_python)