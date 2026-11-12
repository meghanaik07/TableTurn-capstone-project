
import tables
import reservations


def main():
    while True:
        print("\n===== TABLETURN =====")
        print("1. View Tables")
        print("2. Make Reservation")
        print("3. Check Table Availability")
        print("4. View Reservations")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tables.view_tables()

        elif choice == "2":
            reservations.book_reservation()

        elif choice == "3":
            reservations.check_availability()

        elif choice == "4":
            reservations.view_reservations()

        elif choice == "5":
            print("Thank you for using TableTurn!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

