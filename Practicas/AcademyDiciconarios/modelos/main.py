from alumno import GestionarAlumnos
from curso import InterfazCursos


while True:
    print("\n============= BIENVENIDO A ISW ACADEMY =============\n")
    print("¿Qué acción desea llevar cabo?")
    print("1. Cursos")
    print("2. Alumnos")
    print("3. Salir")

    op = int(input("Ingrese la opción: "))

    match op:
        case 1:
            InterfazCursos()
        case 2:
            GestionarAlumnos()
        case 3:
            print("Saliendo de ISW Academy..")
            break
        case _:
            print("Por favor ingrese una respuesta válida.") 



            
