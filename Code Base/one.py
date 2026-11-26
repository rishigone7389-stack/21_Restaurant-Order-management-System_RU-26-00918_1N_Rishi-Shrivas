"""
PS 21 - Restaurant Order Management System
Console application: select a table, take orders, view the running
order and generate the final bill with service charge and GST.
"""


# BLOCK 1: Constants and data storage

MENU = {"Burger": 100, "Pizza": 200, "Coffee": 50}   # dictionary
TOTAL_TABLES = 20
SERVICE_RATE = 0.10    # 10%
GST_RATE = 0.05        # 5%

# One list per table. Index 0 is unused so table 5 -> orders[5].
# Each list holds [item_name, quantity] pairs.
orders = [[] for _ in range(TOTAL_TABLES + 1)]



# BLOCK 2: Menu display

def show_menu():
    print("\n----------- MENU -----------")
    for item, price in MENU.items():
        print(f"{item:<10} Rs.{price}")
    print("----------------------------")



# BLOCK 3: Input validation functions

def get_table():
    """Keep asking until a valid table number (1-20) is entered."""
    while True:
        value = input("Enter table number (1-20): ").strip()
        if value.isdigit() and 1 <= int(value) <= TOTAL_TABLES:
            return int(value)
        print("Invalid table number. Enter a number between 1 and 20.")


def get_item(text):
    """Return the proper menu name for the typed text, or None."""
    name = text.strip().title()          # 'burger' -> 'Burger'
    if name in MENU:
        return name
    print("Item not on the menu. Available: Burger, Pizza, Coffee")
    return None


def get_quantity():
    """Keep asking until a whole number greater than 0 is entered."""
    while True:
        value = input("Quantity: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Invalid quantity. Enter a whole number.")



# BLOCK 4: Taking orders (loop for multiple items)

def add_items(table):
    print(f"\nTaking order for Table {table} (type 'done' to finish)")
    while True:
        text = input("Order item: ").strip()
        if text.lower() == "done":
            break
        item = get_item(text)
        if item is None:                 # invalid item -> ask again
            continue
        qty = get_quantity()

        # If the item is already ordered, increase its quantity
        for entry in orders[table]:
            if entry[0] == item:
                entry[1] += qty
                break
        else:
            orders[table].append([item, qty])

        print(f"{item} x{qty} added to Table {table} | Amount: {MENU[item] * qty}")
        view_order(table)



# BLOCK 5: Running order

def view_order(table):
    if not orders[table]:
        print(f"No items ordered yet for Table {table}.")
        return
    print(f"--- Running order: Table {table} ---")
    for item, qty in orders[table]:
        print(f"{item} x{qty} = {MENU[item] * qty}")



# BLOCK 6: Billing

def generate_bill(table):
    if not orders[table]:
        print(f"Table {table} has no orders, nothing to bill.")
        return

    subtotal = sum(MENU[item] * qty for item, qty in orders[table])
    service = subtotal * SERVICE_RATE
    gst = subtotal * GST_RATE
    total = subtotal + service + gst

    print("\n========== BILL ==========")
    print(f"Table: {table}")
    print(" | ".join(f"{item} x{qty} = {MENU[item] * qty}"
                     for item, qty in orders[table]))
    print("-" * 26)
    print(f"Subtotal: {subtotal}")
    print(f"Service charge (10%): {service:.2f}")
    print(f"GST (5%): {gst:.2f}")
    print(f"Total: {total:.2f}")
    print("==========================")

    orders[table] = []     # table is free for the next customer



# BLOCK 7: Main menu loop

def main():
    print("=== Restaurant Order Management System ===")
    show_menu()
    while True:
        print("\n1. Take order  2. View running order  3. Generate bill  4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_items(get_table())
        elif choice == "2":
            view_order(get_table())
        elif choice == "3":
            generate_bill(get_table())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2, 3 or 4.")



# BLOCK 8: Program entry point

if __name__ == "__main__":
    main()
