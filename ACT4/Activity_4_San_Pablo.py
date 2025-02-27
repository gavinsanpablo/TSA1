import csv

def calculate_grade(class_standing, major_exam):
    return 0.6 * class_standing + 0.4 * major_exam

def sort_by_last_name(student_records):
    return sorted(student_records, key=lambda record: record[1][1])

def sort_by_grade(student_records):
    return sorted(student_records, key=lambda record: calculate_grade(record[2], record[3]), reverse=True)

def show_student_record(student_records, student_id):
    for record in student_records:
        if record[0] == student_id:
            print(f"Student ID: {record[0]}")
            print(f"Name: {record[1][0]} {record[1][1]}")
            print(f"Class Standing: {record[2]}")
            print(f"Major Exam: {record[3]}")
            print(f"Final Grade: {calculate_grade(record[2], record[3]):.2f}")
            return
    print("Student not found.")

def add_record(student_records):
    student_id = int(input("Enter Student ID (6 digits): "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    student_records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added.")

def edit_record(student_records, student_id):
    for i, record in enumerate(student_records):
        if record[0] == student_id:
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            student_records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated.")
            return
    print("Student not found.")

def delete_record(student_records, student_id):
    for i, record in enumerate(student_records):
        if record[0] == student_id:
            del student_records[i]
            print("Record deleted.")
            return
    print("Student not found.")

def open_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            student_records = []
            for row in reader:
                student_id = int(row[0])
                first_name = row[1]
                last_name = row[2]
                class_standing = float(row[3])
                major_exam = float(row[4])
                student_records.append((student_id, (first_name, last_name), class_standing, major_exam))
            print("File opened successfully.")
            return student_records
    except FileNotFoundError:
        print("File not found.")
        return []

def save_file(filename, student_records):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
            for record in student_records:
                writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])
            print("File saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    student_records = []
    filename = "student_records.csv" 

    while True:
        print("\n--- Student Record Management ---")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students (Order by Last Name)")
        print("5. Show All Students (Order by Grade)")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            student_records = open_file(filename)
        elif choice == '2':
            save_file(filename, student_records)
        elif choice == '3':
            new_filename = input("Enter new filename to save as: ")
            save_file(new_filename, student_records)
        elif choice == '4':
            sorted_records = sort_by_last_name(student_records)
            for record in sorted_records:
                print(f"{record[1][1]}, {record[1][0]} (ID: {record[0]})")
        elif choice == '5':
            sorted_records = sort_by_grade(student_records)
            for record in sorted_records:
                print(f"{record[1][1]}, {record[1][0]} (ID: {record[0]}) - Grade: {calculate_grade(record[2], record[3]):.2f}")
        elif choice == '6':
            student_id = int(input("Enter Student ID: "))
            show_student_record(student_records, student_id)
        elif choice == '7':
            add_record(student_records)
        elif choice == '8':
            student_id = int(input("Enter Student ID to edit: "))
            edit_record(student_records, student_id)
        elif choice == '9':
            student_id = int(input("Enter Student ID to delete: "))
            delete_record(student_records, student_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()