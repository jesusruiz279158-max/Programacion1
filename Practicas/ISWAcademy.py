# --- ISW Academy - Gestor de Cursos ---

lista_cursos = []

def buscar_curso(nombre_curso):

    for curso in lista_cursos:
        if curso["nombre"].lower() == nombre_curso.lower():
            return curso  # Devuelve el curso (el diccionario)
    return None  # No se encontró el curso

# --- Funciones para las Opciones del Menú ---

def agregar_curso():
    """Punto 1 y 2: Agrega un nuevo curso a la lista_cursos."""
    print("\n--- 1. Agregar Nuevo Curso ---")
    nombre = input("Nombre del curso: ")
    
    # Verificamos si el curso ya existe
    if buscar_curso(nombre):
        print(f"¡Error! El curso '{nombre}' ya existe.")
        return

    aula = input("Aula asignada: ")
    instructor = input("Nombre del instructor: ")
    
    # Creamos el nuevo curso como un diccionario
    nuevo_curso = {
        "nombre": nombre,
        "aula": aula,
        "instructor": instructor,
        "alumnos": []  # La lista de alumnos empieza vacía
    }
    
    # Agregamos el diccionario a nuestra lista principal
    lista_cursos.append(nuevo_curso)
    print(f"¡Curso '{nombre}' agregado con éxito!")

def modificar_curso():
    """Punto 1 y 4: Modifica instructor o aula de un curso."""
    print("\n--- 2. Modificar Curso ---")
    nombre = input("Nombre del curso que deseas modificar: ")
    
    curso = buscar_curso(nombre)
    
    if curso is None:
        print(f"¡Error! No se encontró el curso '{nombre}'.")
        return

    print(f"Modificando el curso: {curso['nombre']}")
    print("¿Qué deseas modificar?")
    print("  a) Instructor")
    print("  b) Aula")
    opcion = input("Elige una opción (a/b): ").lower()

    if opcion == 'a':
        nuevo_instructor = input("Nuevo nombre del instructor: ")
        curso["instructor"] = nuevo_instructor
        print("¡Instructor actualizado!")
    elif opcion == 'b':
        nueva_aula = input("Nueva aula: ")
        curso["aula"] = nueva_aula
        print("¡Aula actualizada!")
    else:
        print("Opción no válida.")

def eliminar_curso():
    """Punto 1: Elimina un curso de la lista."""
    print("\n--- 3. Eliminar Curso ---")
    nombre = input("Nombre del curso que deseas eliminar: ")
    
    curso = buscar_curso(nombre)
    
    if curso is None:
        print(f"¡Error! No se encontró el curso '{nombre}'.")
        return
        
    # Usamos .remove() para quitar el diccionario de la lista
    lista_cursos.remove(curso)
    print(f"¡Curso '{nombre}' eliminado con éxito!")

def gestionar_alumnos():
    """Punto 4 y 5: Agrega, elimina o muestra alumnos de un curso."""
    print("\n--- 4. Gestionar Alumnos ---")
    nombre_curso = input("Nombre del curso para gestionar alumnos: ")
    
    curso = buscar_curso(nombre_curso)
    
    if curso is None:
        print(f"¡Error! No se encontró el curso '{nombre_curso}'.")
        return

    print(f"Gestionando alumnos de: {curso['nombre']}")
    print("  a) Agregar alumno")
    print("  b) Eliminar alumno")
    print("  c) Mostrar listado de alumnos (Punto 5)")
    opcion = input("Elige una opción (a/b/c): ").lower()

    if opcion == 'a':
        nombre_alumno = input("Nombre del nuevo alumno: ")
        curso["alumnos"].append(nombre_alumno)
        print(f"¡Alumno '{nombre_alumno}' inscrito en {curso['nombre']}!")
        
    elif opcion == 'b':
        nombre_alumno = input("Nombre del alumno a dar de baja: ")
        if nombre_alumno in curso["alumnos"]:
            curso["alumnos"].remove(nombre_alumno)
            print(f"¡Alumno '{nombre_alumno}' dado de baja de {curso['nombre']}!")
        else:
            print(f"¡Error! El alumno '{nombre_alumno}' no está en este curso.")
            
    elif opcion == 'c':
        print(f"\n--- Listado de Alumnos en {curso['nombre']} ---")
        if not curso["alumnos"]:
            print(" (No hay alumnos inscritos en este curso) ")
        else:
            for alumno in curso["alumnos"]:
                print(f"  - {alumno}")
    else:
        print("Opción no válida.")

def mostrar_informacion_cursos():
    """Punto 2 y 3: Muestra detalles de todos los cursos y el conteo de alumnos."""
    print("\n--- 5. Información de Todos los Cursos ---")
    
    if not lista_cursos:
        print("Aún no hay cursos registrados.")
        return

    for curso in lista_cursos:
        print("----------------------------------------")
        print(f"Curso:      {curso['nombre']}")
        print(f"Aula:       {curso['aula']}")
        print(f"Instructor: {curso['instructor']}")
        
        # Punto 3: Saber cuántos están inscritos
        conteo = len(curso['alumnos'])
        print(f"Inscritos:  {conteo} alumnos")
        print("----------------------------------------")

def mostrar_menu():
    """Muestra el menú principal 'atractivo'."""
    print("\n================================")
    print("   Gestor de Cursos ISW Academy   ")
    print("================================")
    print("1. Agregar curso")
    print("2. Modificar curso (instructor o aula)")
    print("3. Eliminar curso")
    print("4. Gestionar alumnos (inscribir, dar baja, ver lista)")
    print("5. Mostrar información de todos los cursos")
    print("6. Salir")
    print("================================")

# --- Bucle Principal del Programa ---
def main():
    """Función principal que ejecuta el menú."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '1':
            agregar_curso()
        elif opcion == '2':
            modificar_curso()
        elif opcion == '3':
            eliminar_curso()
        elif opcion == '4':
            gestionar_alumnos()
        elif opcion == '5':
            mostrar_informacion_cursos()
        elif opcion == '6':
            print("\n¡Gracias por usar el gestor de ISW Academy! Adiós. 👋")
            break  # Termina el bucle while y el programa
        else:
            print("\n¡Opción no válida! Por favor, elige un número del 1 al 6.")

# --- Ejecutar el programa ---
if __name__ == "__main__":
    main()