# Contact Book CLI

A command-line contact management application built with Python. Store, manage, and organize your contacts with a simple and intuitive interface.

## 📚 Overview

This project demonstrates:
- File I/O operations (JSON)
- Data persistence
- Command-line interface (CLI)
- CRUD operations (Create, Read, Update, Delete)
- Data validation
- Error handling
- Unit testing

## 🎯 Features

✅ Add new contacts  
✅ View all contacts  
✅ Search contacts by name  
✅ Update contact information  
✅ Delete contacts  
✅ Save/load contacts from JSON file  
✅ Input validation  
✅ Error handling  
✅ Unit tests  

## 📂 Project Structure

```
Contact_Book_Cli/
├── main.py              # Main application
├── test_main.py         # Unit tests
├── contacts.json        # Contact data storage
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Installation

1. Navigate to project directory:
```bash
cd Contact_Book_Cli
```

2. Create virtual environment (optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Run the application:
```bash
python main.py
```

## 💻 Usage

### Main Menu
```
Contact Book Menu:
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

### Example Operations

**Add a Contact**:
```
Choose option: 1
Enter name: John Doe
Enter phone: 555-1234
Enter email: john@example.com
Contact added successfully!
```

**View All Contacts**:
```
Choose option: 2
All Contacts:
- John Doe (555-1234, john@example.com)
- Jane Smith (555-5678, jane@example.com)
```

**Search Contact**:
```
Choose option: 3
Enter name to search: John
Found: John Doe (555-1234, john@example.com)
```

**Update Contact**:
```
Choose option: 4
Enter name to update: John Doe
Enter new phone: 555-9999
Contact updated successfully!
```

**Delete Contact**:
```
Choose option: 5
Enter name to delete: John Doe
Contact deleted successfully!
```

## 📊 Contact Data Structure

Each contact is stored as:
```json
{
  "name": "John Doe",
  "phone": "555-1234",
  "email": "john@example.com"
}
```

### Sample contacts.json
```json
[
  {
    "name": "John Doe",
    "phone": "555-1234",
    "email": "john@example.com"
  },
  {
    "name": "Jane Smith",
    "phone": "555-5678",
    "email": "jane@example.com"
  }
]
```

## 🛠️ Core Functions

### main.py Functions

**`add_contact()`**
- Collects user input
- Validates data
- Adds new contact to list
- Saves to JSON file

**`view_contacts()`**
- Displays all stored contacts
- Formatted output
- Shows contact details

**`search_contact()`**
- Searches by contact name
- Case-insensitive search
- Returns matching contacts

**`update_contact()`**
- Finds contact by name
- Updates specific fields
- Saves changes

**`delete_contact()`**
- Removes contact from list
- Confirms deletion
- Updates storage

**`load_contacts()`**
- Reads from contacts.json
- Parses JSON data
- Returns contact list

**`save_contacts()`**
- Writes contacts to JSON
- Maintains data persistence
- Handles file I/O

## 🧪 Testing

Run unit tests:
```bash
python -m pytest test_main.py
```

Or using unittest:
```bash
python -m unittest test_main.py
```

### Test Coverage

`test_main.py` includes tests for:
- Adding contacts
- Viewing contacts
- Searching contacts
- Updating contacts
- Deleting contacts
- File I/O operations

Example test:
```python
def test_add_contact(self):
    contact = {"name": "Test User", "phone": "555-0000", "email": "test@example.com"}
    contacts = add_contact(contact)
    self.assertIn(contact, contacts)
```

## 📝 Features Explanation

### Data Persistence
- Contacts saved in `contacts.json`
- Automatically loads on startup
- Survives application restarts

### Input Validation
- Name: Non-empty string
- Phone: Valid phone format
- Email: Valid email format

### Error Handling
- File not found errors
- Invalid input handling
- JSON parsing errors
- Duplicate contact prevention

## 🔧 Enhancement Ideas

1. **Advanced Search**
   - Search by phone or email
   - Multiple criteria search
   - Wildcard search

2. **Data Management**
   - Export to CSV
   - Import from CSV
   - Backup functionality

3. **UI Improvements**
   - Better formatting
   - Colored output
   - Table display

4. **Features**
   - Contact groups/categories
   - Favorites/starred contacts
   - Contact notes
   - Birthday tracking
   - Address storage

5. **Technical**
   - Database instead of JSON
   - Encryption for sensitive data
   - User accounts
   - Web interface

## 📚 Code Example

```python
# Adding a contact
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    # Validation
    if not name or not phone or not email:
        print("Error: All fields are required!")
        return
    
    # Create contact
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    # Add to list
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")
```

## 🎓 Learning Topics

✅ File I/O operations  
✅ JSON handling  
✅ Data structures  
✅ CLI design  
✅ CRUD operations  
✅ Input validation  
✅ Error handling  
✅ Unit testing  
✅ User interaction  
✅ Data persistence  

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| contacts.json not found | File created automatically on first run |
| JSON decode error | Check contacts.json syntax |
| Permission denied | Check file permissions |
| Duplicate contacts | Add validation check |

## 📖 Standard Input/Output

### Menu-Driven Interface
- Clear display of options
- User-friendly prompts
- Confirmation messages
- Error messages
- Status updates

## 🚀 Running the Application

**Start the application**:
```bash
python main.py
```

**Run tests**:
```bash
python -m pytest test_main.py -v
```

**Run with verbose output**:
```bash
python -m pytest test_main.py -v --tb=short
```

## 🌟 Best Practices Demonstrated

- Function decomposition
- Error handling
- Input validation
- Data persistence
- Testing
- Code organization
- Clear documentation
- User-friendly interface

## 📝 Notes

- Contact data is stored in `contacts.json`
- Application creates file if it doesn't exist
- Each contact requires: name, phone, email
- Search is case-insensitive
- Modify code to add more fields as needed

## 🎯 Next Steps

1. Run the application
2. Add some contacts
3. Test all features
4. Review the code
5. Add new features
6. Write additional tests
7. Improve the interface

---

**Happy Contact Managing! 📇**
