def main() -> None:
    while True:
        print("""
    ===== Student Management System =====

    1. Add Student
    2. View Students
    3. Exit
    """)

        try:
            n = int(input("Enter your choice: "))

            if n == 3:
                print("Goodbye!")
                return
            elif n == 1:
                print("Add Student feature coming soon!")
            elif n == 2:
                print("View Students feature coming soon!")
            else:
                print("Invalid choice. Please try again!")

        except ValueError:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()