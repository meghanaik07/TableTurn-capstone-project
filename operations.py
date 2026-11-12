
import tables
import reservations
from datetime import datetime, timedelta, date


def promote_waitlist(table_no):
    now = datetime.now()
    capacity = tables.TABLES[table_no]["capacity"]

    if not reservations.is_table_available(table_no, now):
        return

    for entry in tables.WAITLIST:
        if entry["guests"] <= capacity:
            reservation_id = max(
                (r["id"] for r in tables.RESERVATIONS),
                default=0
            ) + 1

            new_reservation = {
                "id": reservation_id,
                "name": entry["customer"],
                "phone": entry["phone"],
                "guests": entry["guests"],
                "time": now,
                "table": table_no,
                "status": "Seated"
            }

            tables.RESERVATIONS.append(new_reservation)
            tables.WAITLIST.remove(entry)

            print("\nWaitlist customer promoted!")
            print("Customer:", entry["customer"])
            print("Allocated Table:", table_no)
            print("Booking ID:", reservation_id)
            return


def check_no_shows():
    now = datetime.now()
    grace_period = timedelta(minutes=15)

    for reservation in tables.RESERVATIONS:
        if reservation["status"] == "Booked":
            if now > reservation["time"] + grace_period:
                reservation["status"] = "No-show"

                print(
                    "\nNo-show detected:",
                    reservation["name"]
                )

                promote_waitlist(reservation["table"])


def complete_reservation():
    try:
        booking_id = int(input("Enter booking ID: "))
    except ValueError:
        print("Invalid booking ID.")
        return

    for reservation in tables.RESERVATIONS:
        if reservation["id"] == booking_id:
            if reservation["status"] not in ["Booked", "Seated"]:
                print("Reservation is already completed or inactive.")
                return

            reservation["status"] = "Completed"

            tables.DAILY_TURNOVER.append({
                "booking_id": booking_id,
                "table": reservation["table"],
                "date": date.today()
            })

            print("Reservation completed successfully.")
            return

    print("Booking ID not found.")


def daily_turnover_report():
    today = date.today()

    completed = [
        record for record in tables.DAILY_TURNOVER
        if record["date"] == today
    ]

    print("\n===== DAILY TABLE TURNOVER =====")
    print("Date:", today)
    print("Total completed bookings:", len(completed))

    if not completed:
        print("No completed bookings today.")
        return

    for record in completed:
        print(
            "Booking ID:", record["booking_id"],
            "| Table:", record["table"]
        )
