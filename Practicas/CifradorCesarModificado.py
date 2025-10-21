#Convertidores codigo ascii

#caractereres a números
#print(ord("B")) = 66

#Números a caracteres
#print(chr(65)) = A

frase = str(input("Ingrese la frase que desea cifrar: "))
clave = int(input("Ingrese la clave: "))

#"" sirve para declarar que será una cadena de texto
resultado = ""

#Recorre cada caracter de la frase
for caracter in frase:
    #preguntar si el caracter es una letra o signo
    if caracter.isalpha() == True:
        #Mover el caracter hacia la derecha del alfabeto con  ord()
        valor_ascii = ord(caracter)
        #para letras mayúsculas.    Si está en el rango de entre 99 y 127 es minúscula
        if valor_ascii >= 97 and valor_ascii <= 122:
            limite = ord("z")
        elif valor_ascii >= 65 and valor_ascii <= 91: #65 Porque es el primer mayúsculas y 91 es el ultimo mayús
            limite = ord("Z")
        #Sumar 3 para que se mueva a la derecha del alfabeto
        valor_ascii+=3
        #En el caso de poner 'z o Z'
        if valor_ascii >= limite:
            valor_ascii-=26
        #reconvertir de valor a cadena de texto conm chr()
        valor_ascii = chr(valor_ascii)
    else:
        #Si el caracter no es una letra sino un signo
        valor_ascii+= caracter
    resultado+=valor_ascii
print(resultado)