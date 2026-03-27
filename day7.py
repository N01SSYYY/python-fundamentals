def add_student(students):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

students = {}
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student(students)
        
    elif choice == "2":
        for name, marks in students.items():
            print(name, marks)

    elif choice == "3":
        break

    else:
        print("Invalid choice")

for name, marks in students.items():
    print(f"{name} : {marks}")

