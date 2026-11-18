def validate_name(name: str) -> None:
    if not name.strip():
        raise ValueError("Invalid name")
    if not any(char.isalpha() for char in name):
        raise ValueError("Name should contain letters")

def validate_grade(grade: int) -> None:
    if grade < 0 or grade > 100:
        raise ValueError("Invalid grade")


class Student:
    def __init__(self, name: str, grade: int):
        validate_name(name)
        validate_grade(grade)
        self.name = name
        self.grade = grade