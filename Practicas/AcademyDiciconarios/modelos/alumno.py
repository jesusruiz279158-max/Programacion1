from curso import BuscarCurso

def GestionarAlumnos():
    print("\n==========2. Gestionar Alumnos==========\n")
    nombre_curso = input("Ingrese el nombre del curso para gestionar alumnos: ")

    curso = BuscarCurso(nombre_curso)

    if curso is None:
        print(f"¡Error! No se ha encontrado el curso '{nombre_curso}'.")
        return
    
    print(f"=====Gestionando alumnos de: {curso['nombre']}=====")
    print("a) Agregar alumnos")
    print("b) Eliminar alumnos")
    print("c) Mostrar listado de alumnos")

    opcion = input("Eliga una opcion (a/b/c): " ).lower()

    if opcion == 'a':
        nombre_alumno = input("NOmbre del nuevo alumno")
        curso["alumnos"].append(nombre_alumno)
        print(f"Alumno{nombre_alumno} inscrito en {curso['nombre']}")

    elif opcion == 'b':
        nombre_alumno = input("NOmbre del alumno a dar de baja: ")
        if nombre_alumno in curso["alumnos"]:
            curso["alumnos"].remove(nombre_alumno)
            print(f"Alumno '{nombre_alumno}' dado de baja de {curso['nombre']}")
        else:
            print(f"Error el alumno '{nombre_alumno}' no está en este curso")

    elif opcion == 'c':
        print(f"\n ----- Listado de alumnos en {curso['nombre']}-----")
        if not curso["alumnos"]:
            print("No hay alumnos inscritos en este curso.")
        else:
            for alumno in curso["alumnos"]:
                print(f" - {alumno}")
    else:
        print("Por favor ingrese una opción valida.")

