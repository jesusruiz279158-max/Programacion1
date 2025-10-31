from curso import BuscarCurso, cursos

def GestionarAlumnos():

    print("\n========== Gestionar Alumnos ==========\n") 
    nombre_curso = input("Ingrese el nombre del curso para gestionar alumnos: ")

    # --- Buscar la LLAVE del curso ---
    llave_curso = BuscarCurso(nombre_curso)

    # --- Validar el curso ---
    if llave_curso is None:
        print(f"¡Error! No se ha encontrado el curso '{nombre_curso}'.")
        return 
    
    # --- Obtener los DETALLES del curso ---
    curso_detalles = cursos[llave_curso]
    
    print(f"===== Gestionando alumnos de: {llave_curso} =====")
    print("a) Agregar alumno")
    print("b) Eliminar alumno")
    print("c) Mostrar listado de alumnos")

    opcion = input("Elija una opcion (a/b/c): " ).lower() 

    if opcion == 'a':
        nombre_alumno = input("Nombre del nuevo alumno: ") 
        
        # --- Modificar la lista correcta ---
        curso_detalles["alumnos"].append(nombre_alumno)
        print(f"¡Alumno '{nombre_alumno}' inscrito en {llave_curso}!")

    elif opcion == 'b':
        nombre_alumno = input("Nombre del alumno a dar de baja: ")
        
        if nombre_alumno in curso_detalles["alumnos"]:
            curso_detalles["alumnos"].remove(nombre_alumno)
            print(f"Alumno '{nombre_alumno}' dado de baja de {llave_curso}")
        else:
            print(f"Error: el alumno '{nombre_alumno}' no está en este curso")

    elif opcion == 'c':
        print(f"\n ----- Listado de alumnos en {llave_curso} -----")
        
        if not curso_detalles["alumnos"]:
            print("No hay alumnos inscritos en este curso.")
        else:
            for alumno in curso_detalles["alumnos"]:
                print(f" - {alumno}")
    else:
        print("Error: Por favor ingrese una opción valida (a, b, o c).")

