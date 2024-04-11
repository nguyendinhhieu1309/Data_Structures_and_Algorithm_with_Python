from Student import Student
from Stack import Stack

# Create an empty stack to store students
student_stack = Stack()

# Function to add a new student to the stack
def add_student():
    id = input("Enter student ID: ")
    # Check if student ID already exists
    for student in student_stack:
        if student.Id == id:
            print("Student ID already exists.")
            return
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    score = float(input("Enter student score: "))
    student = Student(id, name, address, score)
    student_stack.push(student)
    print("Student added successfully.")

# Function to update student information based on code
def update_student():
    id = input("Enter student ID to update: ")
    found = False
    # Check if student ID exists
    temp_stack = Stack()  # Temporary stack to hold updated students
    while not student_stack.isEmpty():
        student = student_stack.pop()
        if student.Id == id:
            name = input("Enter new name: ")
            address = input("Enter new address: ")
            score = float(input("Enter new score: "))
            student.Name = name
            student.Address = address
            student.Score = score
            print("Student information updated successfully.")
            found = True
        temp_stack.push(student)
    # Restore students back to the original stack
    while not temp_stack.isEmpty():
        student_stack.push(temp_stack.pop())
    if not found:
        print("Student not found.")

# Function to delete a student based on student ID
def delete_student():
    id = input("Enter student ID to delete: ")
    found = False
    # Check if student ID exists
    temp_stack = Stack()  # Temporary stack to hold remaining students
    while not student_stack.isEmpty():
        student = student_stack.pop()
        if student.Id == id:
            print("Student deleted successfully.")
            found = True
        else:
            temp_stack.push(student)
    # Restore remaining students back to the original stack
    while not temp_stack.isEmpty():
        student_stack.push(temp_stack.pop())
    if not found:
        print("Student not found.")

# Function to search for a student by ID
def search_student():
    id = input("Enter student ID to search: ")
    found = False
    temp_stack = Stack()  # Temporary stack to hold searched student
    # Check if student ID exists
    while not student_stack.isEmpty():
        student = student_stack.pop()
        if student.Id == id:
            print("Student information:")
            print(student)
            found = True
        temp_stack.push(student)
    # Restore students back to the original stack
    while not temp_stack.isEmpty():
        student_stack.push(temp_stack.pop())
    if not found:
        print("Student not found.")

def show_all_students():
    print("All Students:")
    temp_stack = Stack()
    # Iterate over the stack and display each student
    for student in student_stack:
        print(student)
        temp_stack.push(student)
    # Restore students back to the original stack
    while not temp_stack.isEmpty():
        student_stack.push(temp_stack.pop())

def sortByScore():
    print("All Students:")
    temp_stack = Stack()
    students_list = []
    # Retrieve all students from the stack and store them in a list
    while not student_stack.isEmpty():
        student = student_stack.pop()
        students_list.append(student)
        temp_stack.push(student)
    # Sort the list of students based on their scores (in descending order)
    sorted_students = sorted(students_list, key=lambda s: s.Score, reverse=True) #Muốn sort theo gì sửa score thành cái đó
    # Display each student's information
    for student in sorted_students:
        print(student)
    # Restore students back to the original stack
    while not temp_stack.isEmpty():
        student_stack.push(temp_stack.pop())
# Main program loop
while True:
    print("\nStudent Management Program")
    print("1. Add a new student")
    print("2. Update student information")
    print("3. Delete a student")
    print("4. Search for a student by ID")
    print("5. Show all student")
    print("6. Sort by Score")
    print("7. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        show_all_students()
    elif choice == "6":
        sortByScore()
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
