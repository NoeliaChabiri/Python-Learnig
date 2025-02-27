# Function to greet
# Función para saludar
def greet(name):
    print(f"Hello, {name}!")  # Hola, {name}!

# Function to add two numbers
# Función para sumar dos números
def add(a, b):
    return a + b  # devuelve la suma de a y b

# Function to check if a number is even or odd
# Función para verificar si un número es par o impar
def check_parity(number):
    if number % 2 == 0:
        return "Even"  # Par
    else:
        return "Odd"  # Impar

# Function that uses a `for` loop to iterate over a list
# Función que utiliza un bucle `for` para iterar sobre una lista
def show_list(lst):
    for item in lst:
        print(item)  # Imprime cada elemento de la lista

# Function that uses a `while` loop to count up to a given number
# Función que usa un bucle `while` para contar hasta un número dado
def count_to(number):
    counter = 1
    while counter <= number:
        print(counter)
        counter += 1

# Function that takes a dictionary as a parameter and returns a value from that dictionary
# Función que recibe un diccionario como parámetro y devuelve un valor de ese diccionario
def get_value(dictionary, key):
    return dictionary.get(key, "Key not found")  # Clave no encontrada

# Main function that uses the previous ones
# Función principal que utiliza las anteriores
def main():
    # Input data from user
    # Entrada de datos desde el usuario
    name = input("What is your name? ")  # ¿Cómo te llamas?
    greet(name)
    
    # Add two numbers
    # Sumar dos números
    number1 = float(input("Enter the first number: "))  # Ingresa el primer número
    number2 = float(input("Enter the second number: "))  # Ingresa el segundo número
    print(f"The sum of the numbers is: {add(number1, number2)}")  # La suma de los números es
    
    # Check if a number is even or odd
    # Verificar si un número es par o impar
    number = int(input("Enter a number to check if it's even or odd: "))  # Ingresa un número para verificar si es par o impar
    print(f"The number {number} is {check_parity(number)}")  # El número {number} es {check_parity(number)}
    
    # Show a list
    # Mostrar una lista
    example_list = [1, 2, 3, 4, 5]
    print("Displaying elements from the list:")  # Mostrando elementos de la lista:
    show_list(example_list)
    
    # Count up to a number
    # Contar hasta un número
    count_to(5)
    
    # Use a dictionary
    # Usar un diccionario
    person = {"name": "Juan", "age": 30, "occupation": "Engineer"}  # persona = {"nombre": "Juan", "edad": 30, "ocupacion": "Ingeniero"}
    key = input("What information would you like to get (name, age, occupation)? ")  # ¿Qué información quieres obtener (nombre, edad, ocupacion)?
    print(f"The {key} is: {get_value(person, key)}")  # La {clave} es: {get_value(person, key)}

# Call the main function to run the code
# Llamar a la función principal para ejecutar el código
if __name__ == "__main__":
    main()