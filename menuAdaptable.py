#Función para limpiar pantalla a medida que se entra en opciones
from datetime import datetime, timedelta
import os
import time

def limpiarPantalla():
    """Limpia la pantalla independientemente del sistema operativo."""
    # Usamos os.name para detectar el sistema operativo
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

#Menu
def main():
    
    #modificar dependiendo la necesidad y la cantidad de opciones 
    control = 0  # Variable para controlar el flujo de los menús
    
    while control != 3:

        limpiarPantalla()  # Llamada a la función limpiarPantalla
        print("1- Socios\n2- Alquileres y Devoluciones\n3- Salir")

        # Menú principal
        control = int(input("Elija una opción: "))

        if control == 1:
            while control != 5:
                #modificar dependiendo la necesidad y la cantidad de opciones 5 opciones 1 if 4 elif break
                limpiarPantalla()
                print("1- Ingresar Socio Nuevo\n2- Modificar Socios\n3- Ver Socios\n4- Baja de Socio\n5- Volver al Menú anterior")
                control = int(input("Elija una opción: "))

                if control == 1:
                    limpiarPantalla()
                elif control == 2:
                    limpiarPantalla()
                elif control == 3:
                    limpiarPantalla()
                elif control == 4:
                    limpiarPantalla()
                elif control == 5:
                    break  # Volver al menú anterior

        elif control == 2:
            while control != 3:
                limpiarPantalla()
                print("1- Alquilar Libro\n2- Devolver libro\n3- Volver al Menú anterior")
                control = int(input("Elija una opción: "))

                if control == 1:
                    limpiarPantalla()
                elif control == 2:
                    limpiarPantalla()
                elif control == 3:
                    break  # Volver al menú anterior

        elif control == 3:
            print("Saliendo del sistema...")
            time.sleep(1)  # Pausa para dar tiempo al usuario de leer el mensaje

if __name__ == "__main__":
    main()