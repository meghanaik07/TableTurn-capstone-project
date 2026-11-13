
import tables
import reservations
import waitlist
import operations


def main():
    while True:
        print("\n========== TABLETURN ==========")
        print("1. View Tables")
        print("2. Make Reservation")
        print("3. Check Table Availability")
        print("4. View Reservations")
        print("5. Add Walk-in Customer")
        print("6. View Waitlist")
        print("7. Check No-shows and Promote Customers")
        print("8. Complete Reservation")
        print("9. Daily Table Turnover Report")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                print("\n===== TABLE DETAILS =====")
                tables.view_tables()

            elif choice == "2":
                reservations.book_reservation()

            elif choice == "3":
                reservations.check_availability()

            elif choice == "4":
                reservations.view_reservations()

            elif choice == "5":
                print("\n===== ADD WALK-IN CUSTOMER =====")
                name = input("Enter customer name: ").strip()
                phone = input("Enter 10-digit phone number: ").strip()

                try:
                    guests = int(input("Enter number of guests: "))
                    waitlist.add_to_waitlist(name, phone, guests)
                except ValueError:
                    print("Please enter a valid guest count.")

            elif choice == "6":
                waitlist.display_waitlist()

            elif choice == "7":
                operations.check_no_shows()

            elif choice == "8":
                operations.complete_reservation()

            elif choice == "9":
                operations.daily_turnover_report()

            elif choice == "10":
                print("Thank you for using TableTurn!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 10.")

        except Exception as error:
            print("An error occurred:", error)

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()
