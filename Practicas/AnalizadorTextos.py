#Pedimos un texto para analizar:
texto = input("Por favor introduzca un texto para analizar: ").strip()

#Pedimos 3 letras al usuario:
#letras_input = input("Ahora ingrese 3 letras separadas. Ej: a b c: ")

#Convertimos todo a minusculas.
texto_minusculas = texto.lower()
#letras_a_buscar = [
#letras_input[0].lower(),
#letras_input[1].lower(),
#letras_input[2].lower()]

letra1 = input("ingrese la primera letra: ").lower()
letra2 = input("ingrese la segunda letra: ").lower()
letra3 = input("ingrese la tercera letra: ").lower()


print(f"las letras ingresada fueron: letra 1: {letra1}, letra 2: {letra2}, letra 3: {letra3}.")
print(texto_minusculas)
#print(letras_a_buscar)


