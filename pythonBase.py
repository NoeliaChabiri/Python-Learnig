# Función para saludar
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para verificar si un número es par o impar
def verificar_paridad(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

# Función que utiliza un bucle `for` para iterar sobre una lista
def mostrar_lista(lista):
    for item in lista:
        print(item)

# Función que usa un bucle `while` para contar hasta un número dado
def contar_hasta(numero):
    contador = 1
    while contador <= numero:
        print(contador)
        contador += 1

# Función que recibe un diccionario como parámetro y devuelve un valor de ese diccionario
def obtener_valor(diccionario, clave):
    return diccionario.get(clave, "Clave no encontrada")

# Función principal que utiliza las anteriores
def main():
    # Entrada de datos desde el usuario
    nombre = input("¿Cómo te llamas? ")
    saludar(nombre)
    
    # Sumar dos números
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    print(f"La suma de los números es: {sumar(numero1, numero2)}")
    
    # Verificar si un número es par o impar
    numero = int(input("Ingresa un número para verificar si es par o impar: "))
    print(f"El número {numero} es {verificar_paridad(numero)}")
    
    # Mostrar una lista
    lista_ejemplo = [1, 2, 3, 4, 5]
    print("Mostrando elementos de la lista:")
    mostrar_lista(lista_ejemplo)
    
    # Contar hasta un número
    contar_hasta(5)
    
    # Usar un diccionario
    persona = {"nombre": "Juan", "edad": 30, "ocupacion": "Ingeniero"}
    clave = input("¿Qué información quieres obtener (nombre, edad, ocupacion)? ")
    print(f"La {clave} es: {obtener_valor(persona, clave)}")

# Llamar a la función principal para ejecutar el código
if __name__ == "__main__":
    main()