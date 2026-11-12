
import tables

waitlist = tables.WAITLIST


def validate_waitlist_input(customer, phone, guests):
    if not isinstance(customer, str) or not customer.strip():
        return False

    if not isinstance(phone, str) or not phone.isdigit() or len(phone) != 10:
        return False

    if not isinstance(guests, int) or isinstance(guests, bool) or guests <= 0:
        return False

    return True


def add_to_waitlist(customer, phone, guests):
    if not validate_waitlist_input(customer, phone, guests):
        print("Invalid customer name, phone number or guest count.")
        return None

    queue_number = max(
        (entry["queue_number"] for entry in waitlist),
        default=0
    ) + 1

    entry = {
        "queue_number": queue_number,
        "customer": customer.strip(),
        "phone": phone,
        "guests": guests,
        "estimated_wait": len(waitlist) * 15
    }

    waitlist.append(entry)

    return entry


def display_waitlist():
    if not waitlist:
        print("Waitlist is empty.")
        return

    print("\n--- Current Waitlist ---")

    for entry in waitlist:
        print(
            f"Queue No: {entry['queue_number']} | "
            f"Name: {entry['customer']} | "
            f"Phone: {entry['phone']} | "
            f"Guests: {entry['guests']} | "
            f"Estimated Wait: {entry['estimated_wait']} minutes"
        )
