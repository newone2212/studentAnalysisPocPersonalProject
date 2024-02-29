from src.analysis import calculate_subject_statistics, calculate_overall_average
from src.display import display_subject_statistics, display_overall_average

students_data = [
    {"name": "Alice", "grades": {"math": 85, "science": 90, "history": 78}},
    {"name": "Bob", "grades": {"math": 90, "science": 88, "history": 92}},
    {"name": "Charlie", "grades": {"math": 80, "science": 85, "history": 88}},
]

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate Subject Statistics")
        print("2. Calculate Overall Average for a Student")
        print("3. Calculate Total Number of Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            subject = input("Enter the subject: ")
            subject_found = False
            all_subject_grades = {}  

            for student in students_data:
                if subject in student["grades"]:
                    subject_found = True
                    grades_for_subject = student["grades"][subject]
                    # print(grades_for_subject)
                    #  Update all_subject_grades with the grades for the current student
                    all_subject_grades.update({student['name']: grades_for_subject})

            if subject_found:
                # Calculate and display overall statistics for the subject across all students
                average, highest, lowest = calculate_subject_statistics(all_subject_grades)
                print("\nOverall Statistics for the Subject:")
                display_subject_statistics(subject, average, highest, lowest)

            else:
                print(f"No data found for the subject '{subject}'.")

        elif choice == "2":
            student_name = input("Enter the student's name: ")
            student_found = False

            for student in students_data:
                if student_name.lower() == student["name"].lower():
                    student_found = True
                    overall_average = calculate_overall_average(student)
                    display_overall_average(student_name, overall_average)

            if not student_found:
                print(f"No data found for the student '{student_name}'.")

        elif choice == "3":
            total_students = len(students_data)
            print(f"\nTotal Number of Students: {total_students}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()