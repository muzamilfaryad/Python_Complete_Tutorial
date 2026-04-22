import json


class ContactBook:
    def __init__(self):
        self.contacts = self.load_contacts()

    # ---------- FILE OPERATIONS ----------
    def save_contacts(self):
        with open('contacts.json', 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # ---------- ADD CONTACT ----------
    def add_contact(self, name, phone):
        for contact in self.contacts:
            if contact['name'] == name and contact['phone'] == phone:
                print("Contact already exists!")
                return

        self.contacts.append({'name': name, 'phone': phone})
        print("Contact added successfully.")

    # ---------- SHOW CONTACTS ----------
    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n--- Contact List ---")
        for c in self.contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}")

    # ---------- DELETE CONTACT ----------
    def delete_contact(self, name, phone=None):
        matches = [c for c in self.contacts if c['name'] == name]

        if not matches:
            print("Contact not found.")
            return

        if len(matches) > 1 and phone is None:
            print(f"Multiple contacts found for '{name}'. Please provide phone number.")
            return

        if phone:
            original_len = len(self.contacts)
            self.contacts = [
                c for c in self.contacts
                if not (c['name'] == name and c['phone'] == phone)
            ]

            if len(self.contacts) < original_len:
                print("Specific contact deleted.")
            else:
                print("Contact not found.")
        else:
            self.contacts = [c for c in self.contacts if c['name'] != name]
            print("Contact(s) deleted.")

    # ---------- UPDATE CONTACT ----------
    def update_contact(self, name, new_phone):
        for c in self.contacts:
            if c['name'] == name:
                c['phone'] = new_phone
                print("Contact updated.")
                return

        print("Contact not found.")


# ================= MAIN PROGRAM =================
def main():
    book = ContactBook()

    while True:
        print("\n====== Contact Book CLI ======")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        # ---------- ADD ----------
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            book.add_contact(name, phone)
            book.save_contacts()

        # ---------- SHOW ----------
        elif choice == '2':
            book.show_contacts()

        # ---------- DELETE ----------
        elif choice == '3':
            name = input("Enter name to delete: ").strip()

            # check duplicates
            matches = [c for c in book.contacts if c['name'] == name]

            if len(matches) > 1:
                print("Multiple contacts found with same name.")
                phone = input("Enter phone number: ").strip()
                book.delete_contact(name, phone)
            else:
                book.delete_contact(name)

            book.save_contacts()

        # ---------- UPDATE ----------
        elif choice == '4':
            name = input("Enter name to update: ").strip()
            new_phone = input("Enter new phone: ").strip()
            book.update_contact(name, new_phone)
            book.save_contacts()

        # ---------- EXIT ----------
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()