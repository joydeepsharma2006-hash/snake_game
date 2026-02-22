from database import create_table
from snake_operation import *

create_table()

while True:
    print("\n--- Snake Database System ---")
    print("1. Add Snake")
    print("2. View All Snakes")
    print("3. Search Snake")
    print("4. Update Snake")
    print("5. Delete Snake")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_snake()
    elif choice == "2":
        view_snakes()
    elif choice == "3":
        search_snake()
    elif choice == "4":
        update_snake()
    elif choice == "5":
        delete_snake()  # type: ignore
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")