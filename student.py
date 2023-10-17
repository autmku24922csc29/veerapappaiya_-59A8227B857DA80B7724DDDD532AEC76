Class Student:
    Def __init__(self, name, roll_number, cgpa):
        Self.name = name
        Self.roll_number = roll_number
        Self.cgpa = cgpa

Def sort_students(student_list):
    Sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    Return sorted_students


Students = [
    Student(“Alice”, “A001”, 3.9),
    Student(“Bob”, “B002”, 3.7),
    Student(“Charlie”, “C003”, 3.5),
    Student(“David”, “D004”, 3.8),
]

Sorted_students = sort_students(students)

For student in sorted_students:
    Print(f”Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}”)
