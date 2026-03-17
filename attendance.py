import datetime

# Simple Attendance System

students = []
attendance_records = {}

# Function to add students
def add_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        students.append(name)
        attendance_records[name] = []

# Function to mark attendance
def mark_attendance():
    date = datetime.date.today().strftime("%Y-%m-%d")
    print(f"\nMarking attendance for {date}")
    for student in students:
        status = input(f"Is {student} present? (y/n): ").lower()
        if status == 'y':
            attendance_records[student].append((date, 'Present'))
        else:
            attendance_records[student].append((date, 'Absent'))

# Function to view attendance
def view_attendance():
    for student, records in attendance_records.items():
        print(f"\n{student}'s Attendance:")
        for date, status in records:
            print(f"  {date}: {status}")

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