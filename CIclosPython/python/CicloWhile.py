while True:
    print("\nMiniCalculadora Interactiva")
    print("Elige una opción: ")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

    opcion = input("Elige una opción(1, 2, 3, 4 o 5): ")

    if opcion == '1':
        a = int(input("Ingrese el primer número de la suma: "))
        b = int(input("Ingrese el segundo número de la suma: "))
        Rsuma = a + b
        print("El resultado de la suma es: ", Rsuma)
    elif opcion == '2':
        c = int(input("Ingrese el primer número de la resta: "))
        d = int(input("Ingrese el segundo número de la resta: "))
        Rresta = c - d
        print("El resultado de la suma es: ", Rresta)
    elif opcion == '3':
        e = int(input("Ingrese el primer número de la multiplicación: "))
        f = int(input("Ingrese el segundo número de la multiplicación: "))
        Rmult = e * f
        print("El resultado de la suma es: ", Rmult)
    elif opcion == '4':
        g = int(input("Ingrese el primer número de la división: "))
        h = int(input("Ingrese el segundo número de la división: "))
        Rdiv = g / h
        print("El resultado de la suma es: ", Rdiv)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("opción invalida. Inténtelo de nuevo.")