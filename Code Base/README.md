# Restaurant Order Management System (PS 21)

A console-based Python application for a restaurant. A waiter selects a table, takes orders from the menu, views the running order and generates the final bill with service charge and GST.

**Course:** B.Tech Computer Science and Engineering, First Semester
**University:** Rungta International Skills University
**Language:** Python 3
**Concepts used:** Lists, Dictionaries, Loops, Billing

---

## Features

- Fixed menu stored in a dictionary
- 20 tables, with the orders of each table stored in a list
- Add multiple items to a table using a loop
- Running order shown after every item is added
- Bill with subtotal, service charge (10%), GST (5%) and grand total
- Input validation for table number, item name and quantity
- Table is cleared automatically after the bill is generated

## Menu

| Item   | Price (Rs.) |
|--------|-------------|
| Burger | 100         |
| Pizza  | 200         |
| Coffee | 50          |

Service charge is 10% and GST is 5%. Both are calculated on the subtotal.

## Requirements

- Python 3.6 or later
- No external libraries needed

## How to Run

```bash
git clone <your-repository-url>
cd <repository-folder>
python restaurant_order_system.py
```

## How to Use

1. Run the program. The menu and options are displayed.
2. Choose an option:

| Option | Action                               |
|--------|--------------------------------------|
| 1      | Take order (select table, add items) |
| 2      | View running order of a table        |
| 3      | Generate bill for a table            |
| 4      | Exit                                 |

3. In option 1, type the item name and quantity. Type `done` when finished.

## Sample Output

```
Order item: burger
Quantity: 2
Burger x2 added to Table 3 | Amount: 200
...
========== BILL ==========
Table: 3
Burger x2 = 200 | Pizza x1 = 200 | Coffee x4 = 200
--------------------------
Subtotal: 600
Service charge (10%): 60.00
GST (5%): 30.00
Total: 690.00
==========================
```

## Test Cases

| # | Type | Input | Expected Output | Result |
|---|------|-------|-----------------|--------|
| 1 | Normal | Table 5, Burger, Qty 2 | `Burger x2 added to Table 5 \| Amount: 200` | Pass |
| 2 | Boundary | Table 1, Coffee, Qty 1, generate bill | Subtotal 50, Service 5.00, GST 2.50, Total 57.50 | Pass |
| 3a | Invalid | Item: Pasta | Item not on the menu. Available: Burger, Pizza, Coffee | Pass |
| 3b | Invalid | Quantity: abc | Invalid quantity. Enter a whole number. | Pass |
| 3c | Invalid | Table: 0 | Invalid table number. Enter a number between 1 and 20. | Pass |
| 4 | Valid | Table 3, Burger x2, Pizza x1, Coffee x4, bill | Subtotal 600, Service 60.00, GST 30.00, Total 690.00 | Pass |

## Project Structure

```
.
├── restaurant_order_system.py   # Main program (single file)
├── README.md                    # Project documentation
└── SUMMARY.md                   # Project report / summary
```

## Author

- **Name:** _Your Name_
- **Enrollment No.:** _Your Enrollment Number_
- **Section:** _Your Section_
