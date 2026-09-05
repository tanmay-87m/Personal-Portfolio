import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")
conn.commit()


# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students(name, age, course, marks) VALUES(?,?,?,?)",
        (name, age, course, marks),
    )
    conn.commit()
    print("Student Added Successfully.\n")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No Records Found.\n")
    else:
        print("\nID\tName\tAge\tCourse\tMarks")
        print("-" * 45)
        for student in students:
            print(
                f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}"
            )
        print()


# Search Student
def search_student():
    sid = int(input("Enter Student ID: "))
    cursor.execute("SELECT * FROM students WHERE id=?", (sid,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Marks:", student[4])
        print()
    else:
        print("Student Not Found.\n")


# Update Student
def update_student():
    sid = int(input("Enter Student ID to Update: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (sid,))
    student = cursor.fetchone()

    if student:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = float(input("Enter New Marks: "))

        cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, marks=?
        WHERE id=?
        """, (name, age, course, marks, sid))

        conn.commit()
        print("Student Updated Successfully.\n")
    else:
        print("Student Not Found.\n")


# Delete Student
def delete_student():
    sid = int(input("Enter Student ID to Delete: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (sid,))
    student = cursor.fetchone()

    if student:
        cursor.execute("DELETE FROM students WHERE id=?", (sid,))
        conn.commit()
        print("Student Deleted Successfully.\n")
    else:
        print("Student Not Found.\n")


# Main Menu
while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        conn.close()
        break

    else:
        print("Invalid Choice.\n")