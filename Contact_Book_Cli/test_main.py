import pytest
from main import ContactBook


# ---------- FIXTURE ----------
@pytest.fixture
def book():
    cb = ContactBook()
    cb.contacts = []  # avoid file dependency
    return cb


# ---------- 1. ADD CONTACT ----------
def test_add_contact(book):
    book.add_contact("Ali", "123")
    assert {"name": "Ali", "phone": "123"} in book.contacts


# ---------- 2. ADD DUPLICATE ----------
def test_add_duplicate_contact(book, capsys):
    book.add_contact("Ali", "123")
    book.add_contact("Ali", "123")

    out = capsys.readouterr().out
    assert "Contact already exists!" in out
    assert len(book.contacts) == 1


# ---------- 3. SHOW EMPTY CONTACTS ----------
def test_show_empty_contacts(book, capsys):
    book.show_contacts()

    out = capsys.readouterr().out
    assert "No contacts found." in out


# ---------- 4. SHOW CONTACTS ----------
def test_show_contacts(book, capsys):
    book.add_contact("Ali", "123")
    book.show_contacts()

    out = capsys.readouterr().out
    assert "Ali" in out
    assert "123" in out


# ---------- 5. UPDATE CONTACT ----------
def test_update_contact(book):
    book.add_contact("Ali", "123")
    book.update_contact("Ali", "999")

    assert book.contacts[0]["phone"] == "999"


# ---------- 6. UPDATE NON-EXISTING ----------
def test_update_non_existing(book, capsys):
    book.update_contact("Unknown", "999")

    out = capsys.readouterr().out
    assert "Contact not found." in out


# ---------- 7. DELETE CONTACT ----------
def test_delete_contact(book):
    book.add_contact("Ali", "123")
    book.delete_contact("Ali")

    assert len(book.contacts) == 0


# ---------- 8. DELETE NON-EXISTING ----------
def test_delete_non_existing(book, capsys):
    book.delete_contact("Ghost")

    out = capsys.readouterr().out
    assert "Contact not found." in out


# ---------- 9. DELETE SPECIFIC CONTACT ----------
def test_delete_specific_contact(book):
    book.add_contact("Ali", "123")
    book.add_contact("Ali", "456")

    book.delete_contact("Ali", "123")

    assert len(book.contacts) == 1
    assert book.contacts[0]["phone"] == "456"


# ---------- 10. MULTIPLE CONTACT WARNING ----------
def test_multiple_contacts_warning(book, capsys):
    book.add_contact("Ali", "123")
    book.add_contact("Ali", "456")

    book.delete_contact("Ali")  # no phone given

    out = capsys.readouterr().out
    assert "Multiple contacts found" in out
    assert len(book.contacts) == 2


# ---------- 11. SAVE FUNCTION CALL (BASIC CHECK) ----------
def test_save_contacts_runs(book):
    book.add_contact("Ali", "123")
    book.save_contacts()

    # If no error = pass (basic smoke test)
    assert True