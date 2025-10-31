# Estructura de datos inicial
cursos = {
    "Programacion I": {
        "Instructor": {
            "nombre": "Jorge Norzagaray",
            "titulo": "Ingeniero en software",
            "edad": 36
        },
        "aula": 922,
        "alumnos": [] 
    }
}

def BuscarCurso(NombreCurso):

    for llave_curso in cursos:
        if llave_curso.lower() == NombreCurso.lower():
            return llave_curso 
    return None

def AgregarCurso():

    print("\n================= AGREGAR CURSO =================\n")
    nombre = input("Nombre del nuevo curso: ")
    
    
    if BuscarCurso(nombre) is not None:
        print(f"Error: El curso '{nombre}' ya existe.")
        return 
    
    instructor_nombre = input("Nombre del instructor: ")
    instructor_titulo = input("Título del instructor: ")
    aula = input("Aula asignada (número): ")

    nuevo_curso = {
        "Instructor": {
            "nombre": instructor_nombre,
            "titulo": instructor_titulo,
            "edad": 0
        },
        "aula": int(aula), 
        "alumnos": []
    }
    
    
    cursos[nombre] = nuevo_curso
    
    print("¡Nuevo curso guardado!")
    

def EliminarCurso():

    print("\n================= 2. Eliminar Curso =================\n")
    nombre = input("Ingrese el nombre del curso que desea eliminar: ")
    
    
    llave_a_eliminar = BuscarCurso(nombre)
    
    if llave_a_eliminar: 
        del cursos[llave_a_eliminar]
        print(f"¡Curso '{llave_a_eliminar}' eliminado exitosamente!")
    else:
        print(f"Error: No se encontró el curso '{nombre}'.")

def VerCursos():
    
    print("\n================= LISTA DE CURSOS =================\n")
    if not cursos: 
        print("No hay cursos registrados.")
        return

    
    for nombre_curso, detalles in cursos.items():
        print(f"--- Curso: {nombre_curso} ---")
        print(f"  Aula: {detalles['aula']}")
        print(f"  Instructor: {detalles['Instructor']['nombre']}")
        print(f"  Título: {detalles['Instructor']['titulo']}")
        print("-" * 20)
        
def InterfazCursos():
    while True:
        print("\n================= CURSOS =================\n")
        print("1. Agregar curso.")
        print("2. Eliminar curso.")
        print("3. Ver todos los cursos.")
        print("4. Salir")
        
        op_str = input("Ingrese la opcion que desea llevar a cabo: ")

        try:
            op = int(op_str)
        except ValueError:
            print("Error: Por favor, ingrese solo un número.")
            continue 

        match op:
            case 1:
                AgregarCurso()
            case 2:
                EliminarCurso()
            case 3:
                VerCursos() 
            case 4:
                print("Saliendo de CURSOS...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    InterfazCursos()