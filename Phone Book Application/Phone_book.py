# Dictionary to store contacts
contact = {}

# Function to display the phonebook menu
def display_phonebook():

        print("")
        print("************* CONTACT BOOK **************")
        print("|                                       |")
        print("|                                       |")
        print("|        1. Add New Contact             |")
        print("|        2. Search Contact              |")
        print("|        3. Display Contact             |")
        print("|        4. Edit Contact                |")
        print("|        5. Delete Contact              |")
        print("|        6. Exit                        |")
        print("*****************************************")
        print("")

# Function to display contacts
def display_contact():
    print("Name \t Contact Number")
    for key, value in contact.items():
        print(f"{key} \t {value}")

# Main loop
while True:
    display_phonebook()
    try:
        choice = int(input("Enter your Choice : "))
        if choice == 1:
            name = input("Enter Contact Name : ")
            phone = input("Enter Mobile Number : ")
            contact[name] = phone

        elif choice == 2:
            search_name = input("Enter the contact name : ")
            if search_name in contact:
                print(search_name, "contact number is ", contact[search_name])
            else:
                print("Contact name is not found!")

        elif choice == 3:
            if not contact:
                print("Contact Book is empty")
            else:
                display_contact()

        elif choice == 4:
            edit_contact = input("Enter the contact to be edited : ")
            if edit_contact in contact:
                phone = input("Enter number : ")
                contact[edit_contact] = phone
                print("Contact updated")
                display_contact()
            else:
                print("Name is not found in the contact book")

        elif choice == 5:
            del_contact = input("Enter the name : ")
            if del_contact in contact:
                confirm = input("Do you want to delete this contact Y/N ? ")
                if confirm.lower() == 'y':
                    contact.pop(del_contact)
                    print("Contact deleted")
                else:
                    print("Contact not deleted")
                display_contact()
            else:
                print("Name is not found in contact book")

        elif choice == 6:
            print("Thankyou for using Phone Book Application ")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    except:
        print("ERROR!")