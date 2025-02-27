def createContact(dic):
    # Ask for name and convert it to uppercase
    name = input("Enter the full name: ").upper()

    # Ask for mobile number
    mobile = input("Enter the mobile number: ")

    # Save in the dictionary
    dic[name] = mobile
    print(f"Contact {name} added successfully.")

def modifyContact(dic):
    # Ask for the name of the contact to modify
    name = input("Enter the full name of the contact you want to modify: ").upper()

    # Check if the contact exists
    if name in dic:
        # Ask for the new name
        name2 = input("Enter the new name: ").upper()
        # Ask for the new mobile number
        mobile = input("Enter the new mobile number: ")

        # Modify the dictionary
        dic[name2] = dic.pop(name)  # Change the key from 'name' to 'name2'
        dic[name2] = mobile  # Update the mobile number
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with the name {name}.")

def deleteContact(dic):
    # Ask for the name of the contact to delete
    name = input("Enter the full name of the contact you want to delete: ").upper()

    # Check if the contact exists
    if name in dic:
        del dic[name]  # Delete the contact by its name
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

def viewAgenda(dic):
    # Check if the agenda is empty
    if not dic:
        print("The agenda does not have any saved contacts yet.")
    else:
        print("Contact Agenda:")
        for name, mobile in dic.items():
            print(f"{name}: {mobile}")

# Contact dictionary
contacts = {}

# Main loop
while True:
    print("\nMenu:")
    print("1 - Add Contact")
    print("2 - Modify Contact")
    print("3 - Delete Contact")
    print("4 - View Agenda")
    print("0 - Exit")

    option = input("Select an option: ")

    if option == '1':
        createContact(contacts)
    elif option == '2':
        modifyContact(contacts)
    elif option == '3':
        deleteContact(contacts)
    elif option == '4':
        viewAgenda(contacts)
    elif option == '0':
        print("You have exited the program.")
        break
    else:
        print("Incorrect option. Try again.")
