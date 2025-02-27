def crearContacto(dic):
    # Pedir nombre y convertirlo a mayúsculas
    nombre = input("Ingrese el nombre completo: ").upper()

    # Pedir número de móvil
    movil = input("Ingrese el número del móvil: ")

    # Guardar en el diccionario
    dic[nombre] = movil
    print(f"Contacto {nombre} agregado con éxito.")


def modificarContacto(dic):
    # Pedir nombre del contacto a modificar
    nombre = input("Ingrese el nombre completo del contacto que desea modificar: ").upper()

    # Verificar si el contacto existe
    if nombre in dic:
        # Pedir el nuevo nombre
        nombre2 = input("Ingrese el nuevo nombre: ").upper()
        # Pedir el nuevo número de móvil
        movil = input("Ingrese el nuevo número del móvil: ")

        # Modificar el diccionario
        dic[nombre2] = dic.pop(nombre)  # Cambiar la clave de 'nombre' a 'nombre2'
        dic[nombre2] = movil  # Actualizar el móvil
        print(f"Contacto de {nombre} actualizado con éxito.")
    else:
        print(f"No se encontró el contacto con el nombre {nombre}.")

def eliminarContacto(dic):
    # Pedir nombre del contacto a eliminar
    nombre = input("Ingrese el nombre completo del contacto que desea eliminar: ").upper()

    # Verificar si el contacto existe
    if nombre in dic:
        del dic[nombre]  # Eliminar el contacto por su nombre
        print(f"Contacto de {nombre} eliminado con éxito.")
    else:
        print(f"No se encontró el contacto con el nombre {nombre}.")

def verAgenda(dic):
    # Verificar si la agenda está vacía
    if not dic:
        print("La agenda aún no tiene contactos archivados.")
    else:
        print("Agenda de contactos:")
        for nombre, movil in dic.items():
            print(f"{nombre}: {movil}")

# Diccionario de contactos
contactos = {}

# Bucle principal
while True:
    print("\nMenú:")
    print("1 - Agregar Contacto")
    print("2 - Modificar Contacto")
    print("3 - Eliminar Contacto")
    print("4 - Ver Agenda")
    print("0 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        crearContacto(contactos)
    elif opcion == '2':
        modificarContacto(contactos)
    elif opcion == '3':
        eliminarContacto(contactos)
    elif opcion == '4':
        verAgenda(contactos)
    elif opcion == '0':
        print("Ha salido del programa.")
        break
    else:
        print("Opción incorrecta. Intente de nuevo.")
