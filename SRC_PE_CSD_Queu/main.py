# Your code here
#hoadnt@fe.edu.vn. 15072022
# do not delete these lines
from Student import Student
from MyQueue import MyQueue

class MyList:
    def __init__(self):
        self.students = MyQueue()

    def add_student(self):
        id = input("Enter student ID: ")
        # Check if student ID already exists
        for student in self.students:
            if student.Id == id:
                print("Student ID already exists.")
                return
        name = input("Enter student name: ")
        address = input("Enter student address: ")
        score = float(input("Enter student score: "))
        student = Student(id, name, address, score)
        self.students.enqueue(student)
        print("Student added successfully.")

    def update_student(self):
        id = input("Enter student ID to update: ")
        found = False
        # Check if student ID exists
        for student in self.students:
            if student.Id == id:
                name = input("Enter new name: ")
                address = input("Enter new address: ")
                score = float(input("Enter new score: "))
                student.Name = name
                student.Address = address
                student.Score = score
                print("Student information updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    def delete_student(self):
        id = input("Enter student ID to delete: ")
        found = False
        # Check if student ID exists
        for student in self.students:
            if student.Id == id:
                self.students.remove(student)
                print("Student deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    def search_student(self):
        id = input("Enter student ID to search: ")
        found = False
        # Check if student ID exists
        for student in self.students:
            if student.Id == id:
                print("Student information:")
                print(student)
                found = True
                break
        if not found:
            print("Student not found.")

    def show_all_students(self):
        if self.students.is_empty():
            print("No students found.")
        else:
            print("All Students:")
            for student in self.students:
                print(student)

    def sort_students_by_score(self):
        sorted_students = sorted(self.students, key=lambda x: x.Score) # sort cái j sửa Score thành cái đó
        if len(sorted_students) == 0:
            print("No students found.")
        else:
            print("Students sorted by score:")
            for student in sorted_students:
                print(student)

# Main program loop
student_list = MyList()

while True:
    print("\nStudent Management Program")
    print("1. Add a new student")
    print("2. Update student information")
    print("3. Delete a student")
    print("4. Search for a student by ID")
    print("5. Show all student")
    print("6. Sort by score")
    print("7. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        student_list.add_student()
    elif choice == "2":
        student_list.update_student()
    elif choice == "3":
        student_list.delete_student()
    elif choice == "4":
        student_list.search_student()
    elif choice == "5":
        student_list.show_all_students()
    elif choice == "6":
        student_list.sort_students_by_score()
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")