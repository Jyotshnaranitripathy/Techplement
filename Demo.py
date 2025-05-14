import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not phone.isdigit():
        print("Invalid phone number. Must contain only digits.")
        return

    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Update contact information
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        print("Leave blank if no change.")
        phone = input("New phone number: ").strip()
        email = input("New email address: ").strip()

        if phone:
            if not phone.isdigit():
                print("Invalid phone number.")
                return
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Display all contacts
def list_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            list_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
   
