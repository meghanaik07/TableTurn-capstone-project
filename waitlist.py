
waitlist = []


def validate_waitlist_input(customer, guests):
    if not isinstance(customer, str) or not customer.strip():
        return False

    if not isinstance(guests, int) or isinstance(guests, bool) or guests <= 0:
        return False

    return True


def add_to_waitlist(customer, guests):
    if not validate_waitlist_input(customer, guests):
        print("Invalid customer name or guest count.")
        return None

    queue_number = len(waitlist) + 1

    entry = {
        "queue_number": queue_number,
        "customer": customer.strip(),
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
            f"Guests: {entry['guests']} | "
            f"Estimated Wait: {entry['estimated_wait']} minutes"
        )
