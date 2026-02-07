"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
# Pre-created dictionary
students = {
    "Rahul": 85,
    "Anita": 92,
    "Aman": 78
}

name = input("Enter student name: ")

if name in students:
    print(f"Marks of {name}: {students[name]}")
else:
    print("Error: this student doesn't exist...")
    choice = input("Type 'add' to add this student: ")

    if choice.lower() == "add":
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"Student '{name}' added successfully.")
    else:
        print("Student not added.")

print("\nUpdated Dictionary:")
print(students)
