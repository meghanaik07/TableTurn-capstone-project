
import tables
from datetime import datetime, timedelta


def is_table_available(table_no, booking_time):
    duration = timedelta(minutes=tables.BOOKING_DURATION)

    for reservation in tables.RESERVATIONS:
        if reservation["table"] == table_no:
            if reservation["status"] in ["Booked", "Seated"]:
                existing_start = reservation["time"]
                existing_end = existing_start + duration
                new_end = booking_time + duration

                if booking_time < existing_end and new_end > existing_start:
                    return False

    return True


def book_reservation():
    print("\n===== MAKE RESERVATION =====")

    name = input("Enter customer name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter 10-digit phone number: ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number.")
        return

    try:
        guests = int(input("Enter number of guests: "))
        if guests <= 0:
            print("Guest count must be greater than zero.")
            return

        date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
        booking_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")

        if booking_time <= datetime.now():
            print("Please enter a future date and time.")
            return

    except ValueError:
        print("Invalid input. Please try again.")
        return

    # Best-Fit allocation
    suitable_tables = []

    for table_no, details in tables.TABLES.items():
        if details["capacity"] >= guests:
            if is_table_available(table_no, booking_time):
                suitable_tables.append((details["capacity"], table_no))

    if not suitable_tables:
        print("No suitable table available.")
        return

    suitable_tables.sort()
    capacity, table_no = suitable_tables[0]

    reservation = {
        "id": len(tables.RESERVATIONS) + 1,
        "name": name,
        "phone": phone,
        "guests": guests,
        "time": booking_time,
        "table": table_no,
        "status": "Booked"
    }

    tables.RESERVATIONS.append(reservation)

    print("\nReservation successful!")
    print("Booking ID:", reservation["id"])
    print("Customer Name:", name)
    print("Phone:", phone)
    print("Number of Guests:", guests)
    print("Allocated Table:", table_no)
    print("Table Capacity:", capacity)
    print("Booking Time:", booking_time.strftime("%Y-%m-%d %H:%M"))


def check_availability():
    print("\n===== CHECK AVAILABILITY =====")

    try:
        guests = int(input("Enter number of guests: "))
        date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
        booking_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")

        if guests <= 0 or booking_time <= datetime.now():
            print("Enter valid details and a future date.")
            return

    except ValueError:
        print("Invalid input.")
        return

    available = []

    for table_no, details in tables.TABLES.items():
        if details["capacity"] >= guests:
            if is_table_available(table_no, booking_time):
                available.append(table_no)

    if available:
        print("Available Tables:", available)
    else:
        print("No suitable tables available.")


def view_reservations():
    print("\n===== VIEW RESERVATIONS =====")

    if not tables.RESERVATIONS:
        print("No reservations found.")
        return

    for reservation in tables.RESERVATIONS:
        print("\nBooking ID:", reservation["id"])
        print("Customer:", reservation["name"])
        print("Phone:", reservation["phone"])
        print("Guests:", reservation["guests"])
        print("Table:", reservation["table"])
        print("Time:", reservation["time"].strftime("%Y-%m-%d %H:%M"))
        print("Status:", reservation["status"])

