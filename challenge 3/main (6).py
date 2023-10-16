class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("Alice", "A123", 3.8),
    Student("Bob", "B456", 3.5),
    Student("Charlie", "C789", 3.9),
    Student("David", "D001", 3.7),
]

# Sort the list of students by CGPA in descending order
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")