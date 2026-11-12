

from datetime import datetime, timedelta

# Table details
TABLES = {
    1: {"capacity": 2},
    2: {"capacity": 2},
    3: {"capacity": 4},
    4: {"capacity": 4},
    5: {"capacity": 6},
    6: {"capacity": 8}
}

# Shared project data
RESERVATIONS = []
WAITLIST = []
DAILY_TURNOVER = []

# Booking duration in minutes
BOOKING_DURATION = 90


def view_tables():
    print("\n--- TABLE DETAILS ---")
    for table_no, details in TABLES.items():
        print(f"Table {table_no}: Capacity {details['capacity']}")
