from student import Student, validate_name, validate_grade


def main() -> None:
    students = []
    while True:
        print("""\n===== Student Management System =====
        1. Add Student
        2. View Students
        3. Remove Student
        4. Exit\n""")
        
        try:
            n = int(input("Enter your choice: "))
            if n == 4:
                print("Goodbye!")
                return
            elif n == 1:
                while True:
                    name = input("Student name: ")
                    try:
                        validate_name(name)
                        break
                    except ValueError as e:
                        print(e)
                while True:
                    try:
                        grade = int(input("Student grade: "))
                        validate_grade(grade)
                        break
                    except ValueError as e:
                        print(e)
                student = Student(name, grade)
                students.append(student)
                print("\nStudent added successfully!")
            elif n == 2:
                if students:
                    for student in students:
                        print(f"{student.name} - {student.grade}")
                else:
                    print("\nYou haven't added a student yet!")
            elif n == 3:
                name = input("Student name: ")
                for student in students:
                    if student.name == name:
                        students.remove(student)
                        print("\nStudent removed successfully!")
                        break
                else:
                    print("\nStudent not found.")
            else:
                print("\nEnter valid number")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()