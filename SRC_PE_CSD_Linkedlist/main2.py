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
    print("7. Delete Max")
    print("8. Count")
    print("91. Exit")


def add_new_student_from_txt(student_list):
    with open("student.txt", "r") as file:
        lines = file.readlines()
        id_list = lines[0].strip().split(", ")
        name_list = lines[1].strip().split(", ")
        address_list = lines[2].strip().split(", ")
        score_list = lines[3].strip().split(", ")

        if len(id_list) == len(name_list) == len(address_list) == len(score_list):
            for i in range(len(id_list)):
                student = Student(id_list[i], name_list[i], address_list[i], int(score_list[i]))
                student_list.addStudentLast(student)
            print("Students added successfully.")
        else:
            print("Error: Number of values in each line of student.txt is not consistent.")


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
    if student_list.deleteStudentBefore(student_id):
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
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_new_student_from_txt(student_list)
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
            student_list.traverse1()
        elif choice == "7":
            student_list.deleteStudentWithMaxScore()
        elif choice == "8":
            p = student_list.count()
            print(p)
        elif choice == "9":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
