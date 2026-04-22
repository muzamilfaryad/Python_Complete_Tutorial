# Contact Book CLI

A clean command-line Contact Book built with Python. This project lets you add, view, update, and delete contacts, with JSON-based persistence and test coverage using `pytest`.

## Highlights

- Simple interactive CLI menu
- Persistent storage in `contacts.json`
- Duplicate prevention for exact `name + phone` pairs
- Smart deletion flow for duplicate names
- Update existing contacts by name
- Unit tests for core behaviors and edge cases

## Project Structure

```text
Contact_Book_Cli/
|-- main.py         # Application logic + CLI loop
|-- test_main.py    # Pytest test suite
|-- contacts.json   # Persisted contact data
|-- README.md
```

## Features

### 1. Add Contact
- Adds a contact as:
  - `name`
  - `phone`
- Prevents duplicate entries when both name and phone are identical.

### 2. Show Contacts
- Displays all saved contacts.
- Shows `No contacts found.` when empty.

### 3. Delete Contact
- Deletes by name.
- If multiple contacts share the same name, the CLI asks for phone number to delete the exact match.
- Handles non-existing contacts safely.

### 4. Update Contact
- Updates the phone number for the first matching contact by name.
- Shows a clear message if contact is not found.

### 5. Persistent Data
- Contacts are automatically saved to `contacts.json` after add, delete, and update operations.
- Data is loaded on startup.
- If the JSON file is missing or invalid, the app starts with an empty list.

## Requirements

- Python 3.8+
- `pytest` (for running tests)

Install test dependency:

```bash
pip install pytest
```

## Run the Application

From the `Contact_Book_Cli` directory:

```bash
python main.py
```

You will see this menu:

```text
====== Contact Book CLI ======
1. Add Contact
2. Show Contacts
3. Delete Contact
4. Update Contact
5. Exit
```

## Run Tests

From the `Contact_Book_Cli` directory:

```bash
pytest -q
```

The test suite covers:

- adding contacts
- duplicate detection
- show contacts (empty and populated)
- update existing and non-existing contacts
- delete existing, non-existing, and specific duplicate-name contacts
- multiple-match deletion warning path
- save function smoke check

## Behavior Notes

- Duplicate check is exact for `(name, phone)`.
- Update operation matches by name and updates the first matching entry.
- Delete operation supports precision by phone when duplicate names exist.

## Future Improvements

- Add search by partial name/phone
- Add contact validation (phone format, empty name protection)
- Add sorting and pagination for large lists
- Add export/import options (CSV)
- Add test isolation for file-based operations using temporary files

## License

This project is for internship learning and practice.
