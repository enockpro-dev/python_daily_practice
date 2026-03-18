import datetime

# Simple Attendance System

students = []
attendance_records = {}  # {student: {date: bool}}
attendance_dates = []  # ordered list of dates tracked

# Function to add students
def add_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        students.append(name)
        attendance_records[name] = {}

# Function to mark attendance
def mark_attendance():
    date = datetime.date.today().strftime("%d-%m-%Y")

    if date not in attendance_dates:
        attendance_dates.append(date)

    print(f"\nMarking attendance for {date}")
    for student in students:
        status = input(f"Is {student} present? (y/n): ").strip().lower()
        attendance_records[student][date] = (status == 'y')

    # Automatically view attendance for the day after marking
    view_attendance_for_date(date)

# Function to view attendance
def view_attendance():
    if not attendance_dates:
        print("No attendance has been recorded yet.")
        return

    # Print header
    header = ["Name"] + attendance_dates
    print("\t".join(header))

    # Print each student's row
    for student in students:
        row = [student]
        for date in attendance_dates:
            present = attendance_records[student].get(date, False)
            row.append("✓" if present else "✗")
        print("\t".join(row))

# Function to view attendance for a specific date
def view_attendance_for_date(date):
    if date not in attendance_dates:
        print(f"No attendance recorded for {date}.")
        return

    print(f"Attendance for {date}:")
    for student in students:
        present = attendance_records[student].get(date, False)
        status = "✓" if present else "✗"
        print(f"{student}: {status}")

# Main program
if __name__ == "__main__":
    add_students()
    while True:
        print("\n1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")