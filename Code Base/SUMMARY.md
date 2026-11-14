# Project Summary: Restaurant Order Management System

| Field         | Details                                  |
|---------------|------------------------------------------|
| PS No.        | 21                                       |
| Project Title | Restaurant Order Management System       |
| Language      | Python 3                                 |
| Concepts      | Lists, Dictionaries, Loops, Billing      |
| Student       | _Your Name_ (_Enrollment No._)           |

## 1. Problem Definition

A restaurant needs a simple console application where a waiter can select a table, take orders from the menu, view the running order and generate a final bill including service charge and GST. Menu prices are Burger Rs.100, Pizza Rs.200 and Coffee Rs.50. Tables are numbered 1 to 20. Service charge is 10% and GST is 5%, both on the subtotal.

## 2. Approach

1. **Data storage:** the menu is a dictionary (`item -> price`). Orders are a list of lists, one list per table, each holding `[item, quantity]` pairs.
2. **Validation:** separate functions check the table number (1 to 20), item name (must be on the menu, case-insensitive) and quantity (whole number greater than 0). Each re-prompts until the input is valid.
3. **Order taking:** a `while` loop accepts multiple items for a table until the user types `done`. Repeated items have their quantity merged.
4. **Billing:** subtotal is the sum of price × quantity. Service charge = 10% of subtotal, GST = 5% of subtotal, Total = subtotal + service charge + GST.
5. **Menu-driven interface:** a main loop offers options to take an order, view the running order, generate a bill, or exit.

## 3. Program Structure

| Block | Function(s)            | Purpose                                        |
|-------|------------------------|------------------------------------------------|
| 1     | Constants, `orders`    | Menu dictionary, rates, per-table order lists  |
| 2     | `show_menu()`          | Display the menu                               |
| 3     | `get_table()`, `get_item()`, `get_quantity()` | Input validation        |
| 4     | `add_items()`          | Loop to take multiple items for a table        |
| 5     | `view_order()`         | Show the running order                         |
| 6     | `generate_bill()`      | Calculate and print the bill, clear the table  |
| 7     | `main()`               | Menu-driven main loop                          |
| 8     | `__main__` check       | Program entry point                            |

## 4. Bare Minimum Requirements Checklist

| Requirement                                                   | Status |
|---------------------------------------------------------------|--------|
| Solution in Python 3, single `.py` file, runs from console    | Done   |
| Menu in a dictionary, each table's orders in a list           | Done   |
| Loop to take multiple items and show running order            | Done   |
| Calculate subtotal, service charge, GST, total and print bill | Done   |
| Validate table number, item name and quantity                 | Done   |

## 5. Testing

All four test cases from the problem statement were executed and produced the expected output.

| Test Case | Description | Result |
|-----------|-------------|--------|
| 1 | Normal input: Table 5, Burger x2 gives amount 200 | Pass |
| 2 | Boundary: Table 1, Coffee x1 gives Subtotal 50, Service 5.00, GST 2.50, Total 57.50 | Pass |
| 3 | Invalid: Pasta, `abc`, Table 0 each show the correct error and re-prompt | Pass |
| 4 | Table 3: Burger x2, Pizza x1, Coffee x4 gives Subtotal 600, Service 60.00, GST 30.00, Total 690.00 | Pass |

## 6. Conclusion

The project meets every requirement of PS 21. It applies lists, dictionaries, loops and arithmetic in a practical billing scenario. The validation functions keep the program from crashing on bad input.

**Possible improvements:** add more menu items, save bills to a file, support discounts, or build a graphical interface.
