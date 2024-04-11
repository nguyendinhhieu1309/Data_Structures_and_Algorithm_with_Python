# Your code here
#hoadnt@fe.edu.vn. 15072022
# do not delete these lines
from Student import *
from MyList import *

def print_student(student):
    print("Student ID:", student.Id)
    print("Name:", student.Name)
    print("Address:", student.Address)
    print("Score:", student.Score)

def display_menu():
    print("Student Management Program")
    print("1. Add new student")
    print("2. Update student information")
    print("3. Delete student")
    print("4. Search student by ID")
    print("5. Show all")
    print("6. Sort by score")
    print("7. Exit")

def add_new_student(student_list):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    score = input("Enter student score: ")

    student = Student(student_id, name, address, score)
    student_list.addStudentHead(student)
    print("Student added successfully.")

def update_student_information(student_list):
    student_id = input("Enter student ID: ")
    student = student_list.findStudentById(student_id)
    if student:
        name = input("Enter updated student name: ")
        address = input("Enter updated student address: ")
        score = input("Enter updated student score: ")

        updated_student = Student(student_id, name, address, score)
        student_list.updateStudent(student_id, updated_student)
        print("Student information updated successfully.")
    else:
        print("Student not found.")

def delete_student(student_list):
    student_id = input("Enter student ID: ")
    if student_list.deleteStudent(student_id):
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def search_student_by_id(student_list):
    student_id = input("Enter student ID: ")
    student = student_list.findStudentById(student_id)
    if student:
        print_student(student)
    else:
        print("Student not found.")

def main():
    student_list = MyList()
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_new_student(student_list)
        elif choice == "2":
            update_student_information(student_list)
        elif choice == "3":
            delete_student(student_list)
        elif choice == "4":
            search_student_by_id(student_list)
        elif choice == "5":
            student_list.traverse()
        elif choice == "6":
            student_list.sort()
            student_list.traverse()
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
