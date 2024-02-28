import sqlite3

def create_contact_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            CellNumber TEXT,
            Email TEXT
        )
    """
    )
    conn.commit()

def insert_contact(conn, name, cell_number, email):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO contacts (Name, CellNumber, Email)
        VALUES (?, ?, ?)
    """,
        (name, cell_number, email),
    )
    conn.commit()

def fetch_all_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    return rows

def delete_all_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts")
    conn.commit()

def display_contacts(contacts):
    print("Id\tName\t\t\tCell Number\tEmail")
    print("-" * 60)
    for contact in contacts:
        print(f"{contact[0]}\t{contact[1]}\t\t{contact[2]}\t{contact[3]}")



conn = sqlite3.connect("contact_book.db")

try:
    
    create_contact_table(conn)

    insert_contact(conn, "Hydrogen Helium", "123-456-7890", "hydrogen.helium@email.com")
    insert_contact(conn, "Lithium Beryllium", "987-654-3210", "lithium.beryllium@email.com")
    insert_contact(conn, "Boron Carbon", "555-123-4567", "boron.carbon@email.com")
    insert_contact(conn, "Nitrogen Oxygen", "888-555-1234", "nitrogen.oxygen@email.com")
    insert_contact(conn, "Fluorine Neon", "111-222-3333", "fluorine.neon@email.com")
    
    contacts = fetch_all_contacts(conn)
    display_contacts(contacts)
finally:
    
    delete_all_contacts(conn)

    conn.close()
