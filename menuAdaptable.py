# Function to clear the screen as options are selected
from datetime import datetime, timedelta
import os
import time

def clearScreen():
    """Clears the screen regardless of the operating system."""
    # Use os.name to detect the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

# Menu
def main():
    
    # Modify depending on the need and the number of options
    control = 0  # Variable to control the flow of menus
    
    while control != 3:

        clearScreen()  # Call the clearScreen function
        print("1- Members\n2- Rentals and Returns\n3- Exit")

        # Main menu
        control = int(input("Choose an option: "))

        if control == 1:
            while control != 5:
                # Modify depending on the need and the number of options (5 options, 1 if, 4 elif, break)
                clearScreen()
                print("1- Add New Member\n2- Modify Members\n3- View Members\n4- Remove Member\n5- Go back to Previous Menu")
                control = int(input("Choose an option: "))

                if control == 1:
                    clearScreen()
                elif control == 2:
                    clearScreen()
                elif control == 3:
                    clearScreen()
                elif control == 4:
                    clearScreen()
                elif control == 5:
                    break  # Go back to the previous menu

        elif control == 2:
            while control != 3:
                clearScreen()
                print("1- Rent Book\n2- Return Book\n3- Go back to Previous Menu")
                control = int(input("Choose an option: "))

                if control == 1:
                    clearScreen()
                elif control == 2:
                    clearScreen()
                elif control == 3:
                    break  # Go back to the previous menu

        elif control == 3:
            print("Exiting the system...")
            time.sleep(1)  # Pause to allow the user to read the message

if __name__ == "__main__":
    main()