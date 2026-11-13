# TableTurn: Best-Fit Table Reservation and Waitlist Engine

A Python-based console application designed to simplify restaurant table reservations and restaurant operations. The system uses a Best-Fit allocation approach to assign suitable tables, manages walk-in customers through a waitlist, handles no-shows, and generates a daily table turnover report.

## Team

1. **Namana N (1A24IS131)** – Customer Reservation and Table Management
2. **Megha R Naik (1AT24IS117)** – Waitlist and Restaurant Operations

## How to Run

### Requirements
- Python 3.x
- Visual Studio Code or any Python-supported IDE

### Steps
1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Make sure all Python files are in the same folder.
4. Open the terminal.
5. Run the following command:

   `python main.py`

6. The TableTurn main menu will appear. Select an option by entering its number.

## Features

1. **Table Management:** Stores restaurant table details and their seating capacities.
2. **Best-Fit Table Allocation:** Automatically allocates the smallest suitable available table based on the number of guests.
3. **Reservation Management:** Allows customers to make reservations by entering their name, phone number, date, time, and number of guests.
4. **Table Availability:** Checks whether a suitable table is available for the selected date and time.
5. **Reservation Details:** Displays existing reservations and their booking information.
6. **Walk-in Waitlist:** Allows walk-in customers to be added to the waitlist.
7. **Estimated Waiting Time:** Provides an estimated waiting time for customers in the waitlist.
8. **No-Show Management:** Marks reservations as no-show if the customer does not arrive within the 15-minute grace period when the no-show check is performed.
9. **Automatic Waitlist Promotion:** Promotes a suitable waiting customer when a reservation is marked as a no-show and its table becomes available.
10. **Reservation Completion:** Allows reservations to be marked as completed.
11. **Daily Table Turnover Report:** Displays completed reservations recorded for the current day.

## Sample Run

```text
========== TABLETURN ==========

1. View Tables
2. Make Reservation
3. Check Table Availability
4. View Reservations
5. Add Walk-in Customer
6. View Waitlist
7. Check No-shows and Promote Customers
8. Complete Reservation
9. Daily Table Turnover Report
10. Exit

Enter your choice: 1

===== TABLE DETAILS =====
Table 1: Capacity 2
Table 2: Capacity 2
Table 3: Capacity 4
Table 4: Capacity 4
Table 5: Capacity 6
Table 6: Capacity 8

Enter your choice: 10

Thank you for using TableTurn!
```

## Technologies Used

- Python
- VS Code
- Git and GitHub