#Paso 1
#agregar, eliminar, modificar cursos
cursos = ["Programacion", "Matematicas", "Ingles", ]
def interfaz_inicial():
    while True:
        print("\n-----ISW Academy-----\n")
        print("Elige una opción: ")
        print("1. Cursos.")
        print("2. Salir")

        opcion = input("Eliga una opcion(1, 2): ")

        if opcion == "2":
            print("\nSaliendo de ISW Academy...")
            break

        elif opcion == "1":
            print("\n¿Qué acción desea llevar a cabo?\n")
            print("1. Agregar Curso.")
            print("2. Modificar Curso.")
            print("3. Eliminar Curso.")
            
        else:
                 print("\nPor favor ingrese una opción válida.\n")
        

interfaz_inicial()








#def pestaña_cursos():

#Paso 2
#Desea saber el nombre del curso, aula, instructor y lista de alumnos


#Paso 3
#desea saber cuantos alumnos estan inscritos por curso

#Paso 4
#Modificar Instructore, Aula, dar de alta y baja alumnos 


#Paso 5
#Mostrar el listado de alumnos

#Paso 6
#Interfaz atractiva, solo salir al seleccionar la opcion