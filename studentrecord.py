# File: main_program.py

import os

def add_student():
    while True:
        try:
            name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))

            with open("student_records.txt", "a") as file:
                file.write(f"{name},{grade}\n")
                print(f"Student record added: {name}, Grade: {grade}")

            break  # Exit loop if successful
        except ValueError:
            print("Invalid input. Grade should be a number.")
        except Exception as e:
            print(f"Error: {e}")

def display_students():
    try:
        with open("student_records.txt", "r") as file:
            print("Student Records:")
            for line in file:
                name, grade = line.strip().split(',')
                print(f"Name: {name}, Grade: {grade}")
    except FileNotFoundError:
        print("File not found. No student records available.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        try:
            if choice == '1':
                add_student()
            elif choice == '2':
                display_students()
            elif choice == '3':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
