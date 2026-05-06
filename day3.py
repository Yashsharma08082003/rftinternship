# Phonebook using Dictionary

phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780"
}

# Add Contact
def add_contact(name, number):
    name = name.upper()
    if name in phonebook:
        print("Contact already exists!")
    else:
        phonebook[name] = number
        print("Contact added successfully.")

# Search Contact (Exact + Partial)
def search_contact(name):
    name = name.upper()
    found = False
    
    for contact in phonebook:
        if name in contact:   # Partial search
            print(f"{contact} : {phonebook[contact]}")
            found = True
    
    if not found:
        print(" Contact not found.")

# Delete Contact
def delete_contact(name):
    name = name.upper()
    if name in phonebook:
        del phonebook[name]
        print("🗑️ Contact deleted.")
    else:
        print("Contact not found.")

# Display All Contacts
def display_contacts():
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("\nPhonebook:")
        for name, number in phonebook.items():
            print(f"{name} : {number}")

# Menu-driven program
while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)

    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        display_contacts()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")