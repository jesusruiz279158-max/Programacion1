

listadoCursos = []

def BuscarCurso(NombreCurso):
    for curso in listadoCursos:
        if curso["nombre"].lower() == NombreCurso.lower():
            return curso
    return None

def AgregarCurso():
    print("=====1. Agregar un nuevo curso=====")
    nombre = input("Ingrese el nombre del nuevo curso: ")
    instructor = input("Ingrese el nombre del instructor: ")
    aula = input("Ingrese el aula: ")
    alumnos = []
    curso = [nombre, instructor, aula, alumnos]
    print("¡Nuevo curso guardado!")
    return curso
    
def ModificarCurso():
    print("=====2. Modificar Curso=====")
    nombre = input("Ingrese el nombre del curso que desea modificar: ")
    curso = BuscarCurso(nombre)
    if BuscarCurso(nombre) == curso:
        listadoCursos
    while True:
        print(f"\n---Modificar Curso {nombre}---\n")
        print("¿Qué deseas modificar?: ")
        print("a) Instructor del curso.")
        print("b) Aula del curso.")
        opcion = input("Elige una opción a/b: ").lower()
        
        if opcion == "a":
            nuevoIns = input("Ingrese el nombre del nuevo instructor: ")
            curso["instructor"] = nuevoIns
        elif opcion == "b":
            nuevaAula = input("Ingrese la nueva aula: ")
            curso["aula"] = nuevaAula

def EliminarCurso():
    print("=====3. Eliminar Curso=====")
    nombre = input("Ingrese el nombre del curso que desea eliminar: ")
    curso = BuscarCurso(nombre)
    if BuscarCurso(nombre) == curso:
        listadoCursos.remove(curso)

def MostrarNombres():
    print("=====Mostrar Nombres=====")
    for i in range(len(listadoCursos)):
        print(f"{i} <==> {listadoCursos[i][0]}")
        opcion = int(input("Ingrese el indice del curso"))
        
        listadoCursos[opcion][3].append(input("ingrese el nombre del alumno: "))





def MenuInicial():
    while True:
        print("\n-----¡Bienvendo al gestor de ISW Academy!-----\n")
        print("¿Qué acción desea llevar a cabo?")
        print("1. Agregar un curso.")
        print("2. Modificar un curso.")
        print("3. Eliminar un curso.")

        opcion = int(input("Ingrese la opción que desea llevar a cabo(1, 2, 3): "))

        match opcion:
            case 1:
                AgregarCurso()
            case 2:
                ModificarCurso()
            case 3:
                EliminarCurso()


MenuInicial()