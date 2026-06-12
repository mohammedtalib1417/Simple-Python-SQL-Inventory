import sqlite3

# 1. Connect to the database (It will create a file named store.db automatically)
connection = sqlite3.connect("store.db")
cursor = connection.cursor()

# 2. Create a simple table using SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER
)
""")
connection.commit()

print("--- Inventory System Started ---")

while True:
    print("\n1. Add Item")
    print("2. View All Items")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3): ")
    
    if choice == "1":
        # Get data from user
        item_name = input("Enter item name: ")
        item_qty = input("Enter quantity: ")
        
        # Insert data into SQL table
        cursor.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (item_name, item_qty))
        connection.commit()
        print("✅ Item added successfully!")
        
    elif choice == "2":
        # Fetch data using SQL SELECT query
        cursor.execute("SELECT * FROM items")
        all_items = cursor.fetchall()
        
        print("\n--- Current Inventory ---")
        for row in all_items:
            print(f"ID: {row[0]} | Name: {row[1]} | Quantity: {row[2]}")
            
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

# Close connection when exiting
connection.close()