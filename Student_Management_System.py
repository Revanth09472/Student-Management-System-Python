student={}

def add_student():
    name = input("enter name:")
    marks = int(input("enter marks: "))
    student[name] = marks
    print("student added successfully!")
def view_students():
    for name, marks in student.items():
        print(name, ":", marks)
def search_student():
    name = input("enter name to search:")
    if name in student:
        print(name, ":", student[name])
    else:
        print("student not found")
def delete_student():
    name = input("enter name to delete:")
    if name in student:
        student.pop(name)
        print("student deleted successfully!")
    else:
        print("student not found")

while True:
    print("\n1.add student")
    print("2.view students")
    print("3.search student")
    print("4.delete student")
    print("5.exit")
    choice = int(input("enter choice:"))
    if choice == 1:
        add_student()
    elif choice ==2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("exiting the program...")
        break
    else:
        print("invalid choice, please try again")