import sqlite3
from database import connect
def add_snake():
    conn = connect()
    cursor = conn.cursor()

    name = input("Enter Snake Name: ")
    scientific = input("Enter Scientific Name: ")
    venomous = input("Venomous (Yes/No): ")

    while True:
        try:
            length_input = input("Average Length (meters): ")
            length_input = length_input.replace(",", ".")
            length = float(length_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number (example: 1.0)")

    habitat = input("Habitat: ")
    region = input("Region: ")
    diet = input("Diet: ")
    status = input("Conservation Status: ")

    cursor.execute("""
    INSERT INTO snakes
    (name, scientific_name, venomous, average_length, habitat, region, diet, conservation_status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, scientific, venomous, length, habitat, region, diet, status))

    conn.commit()
    conn.close()

    print("Snake added successfully!")

def view_snakes():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM snakes")
    rows = cursor.fetchall()

    if not rows:
        print("No snakes found.")
    else:
        for row in rows:
            print("-" * 50)
            print("ID:", row[0])
            print("Name:", row[1])
            print("Scientific Name:", row[2])
            print("Venomous:", row[3])
            print("Average Length:", row[4])
            print("Habitat:", row[5])
            print("Region:", row[6])
            print("Diet:", row[7])
            print("Conservation Status:", row[8])

    conn.close()

def search_snake():
    conn = connect()
    cursor = conn.cursor()

    snake_id = input("Enter snake ID to search: ")

    cursor.execute("SELECT * FROM snakes WHERE id = ?", (snake_id,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("\n" + "="*40)
            print("Snake ID:", row[0])
            print("Name:", row[1])
            print("Scientific Name:", row[2])
            print("Venomous:", row[3])
            print("Average Length (m):", row[4])
            print("Habitat:", row[5])
            print("Region:", row[6])
            print("Diet:", row[7])
            print("Conservation Status:", row[8])
            print("="*40)
    else:
        print("No snake found.")

    conn.close()

def delete_snake():
    conn = connect()
    cursor = conn.cursor()

    snake_id = int(input("Enter snake ID to delete: "))

    cursor.execute("DELETE FROM snakes WHERE id = ?", (snake_id,))
    conn.commit()

    print("Snake deleted successfully!")
    conn.close()

def update_snake():
    conn = connect()
    cursor = conn.cursor()

    snake_id = int(input("Enter Snake ID to update: "))

    # First check if snake exists
    cursor.execute("SELECT * FROM snakes WHERE id = ?", (snake_id,))
    snake = cursor.fetchone()

    if not snake:
        print("Snake not found!")
        conn.close()
        return

    print("Enter new details (leave blank to keep old value):")

    name = input(f"Name ({snake[1]}): ") or snake[1]
    scientific = input(f"Scientific Name ({snake[2]}): ") or snake[2]
    venomous = input(f"Venomous ({snake[3]}): ") or snake[3]
    
    length_input = input(f"Average Length ({snake[4]}): ")
    length = float(length_input) if length_input else snake[4]

    habitat = input(f"Habitat ({snake[5]}): ") or snake[5]
    region = input(f"Region ({snake[6]}): ") or snake[6]
    diet = input(f"Diet ({snake[7]}): ") or snake[7]
    status = input(f"Conservation Status ({snake[8]}): ") or snake[8]

    cursor.execute("""
    UPDATE snakes
    SET name = ?,
        scientific_name = ?,
        venomous = ?,
        average_length = ?,
        habitat = ?,
        region = ?,
        diet = ?,
        conservation_status = ?
    WHERE id = ?
    """, (name, scientific, venomous, length, habitat, region, diet, status, snake_id))

    conn.commit()
    conn.close()

    print("Snake updated successfully!")