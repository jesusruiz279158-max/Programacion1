cursos = {
    "Programacion I":{
        "Instructor": {
            "nombre": "Jorge Norzagaray",
            "titulo": "Ingeniero en software",
            "edad": 36
        },
        "aula": 922,
    }
}


def BuscarCurso(NombreCurso):
    for curso in cursos:
        if curso["nombre"].lower() == NombreCurso.lower():
            return curso
    return None

def AgregarCurso():
    nombre = input("Nombre del nuevo curso: ")
    instructor = input("Nombre del instructor: ")
    aula = input("Aula asignada: ")
    alumnos = []
    curso = [nombre, instructor, aula, alumnos]
    print("¡Nuevo curso guardado!")
    return curso



def EliminarCurso():
    print("\n==========3. Eliminar Curso==========\n")
    nombre = input("Ingrese el nombre del curso que desea eliminar: ")
    curso = BuscarCurso(nombre)
    if BuscarCurso(nombre) == curso:
        cursos.remove(curso)



def InterfazCursos():
    while True:
        print("\n================= CURSOS =================\n")
        print("1. Agregar curso.")
        print("2. Eliminar curso.")
        print("3. Salir")
        op = int(input("Ingrese la opcion que desea llevar a cabo: "))

        match op:
            case 1:
                print("\n================= AGREGAR CURSO =================\n")
                AgregarCurso()
            case 2:
                print("\n================= ELIMINAR CURSO =================\n")
                EliminarCurso()
            case 3:
                print("Saliendo de CURSOS...")
                break