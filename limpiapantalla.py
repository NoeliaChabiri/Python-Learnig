# Screen Clear Function | Función de Limpieza de Pantalla

##A function to clear the screen on any operating system
##Una función para limpiar la pantalla en cualquier sistema operativo

## Code | Código

import platform
import os


def limpiarPantalla():
    """
    Limpia la pantalla independientemente del sistema operativo.
    Clears the screen regardless of the operating system.
    """
    # Detectar el sistema operativo | Detect the operating system
    sistema = platform.system()
    
    # Usamos os.name para detectar el sistema operativo | Use os.name to detect the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

