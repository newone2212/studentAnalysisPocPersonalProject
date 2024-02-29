from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from src.analysis import calculate_subject_statistics, calculate_overall_average
from src.display import display_subject_statistics, display_overall_average

students_data = [
    {"name": "Alice", "grades": {"math": 85, "science": 90, "history": 78}},
    {"name": "Bob", "grades": {"math": 90, "science": 88, "history": 92}},
    {"name": "Charlie", "grades": {"math": 80, "science": 85, "history": 88}},
]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate_subject_statistics', methods=['POST'])
def calculate_subject_statistics_route():
    subject = request.form['subject']
    subject_found = False
    all_subject_grades = {}

    for student in students_data:
        if subject in student["grades"]:
            subject_found = True
            grades_for_subject = student["grades"][subject]
            all_subject_grades.update({student['name']: grades_for_subject})

    if subject_found:
        average, highest, lowest = calculate_subject_statistics(all_subject_grades)
        result = {
            "subject": subject,
            "average": average,
            "highest": highest,
            "lowest": lowest
        }
        return jsonify(result)
    else:
        return jsonify({"message": f"No data found for the subject '{subject}'."})

@app.route('/calculate_overall_average', methods=['POST'])
def calculate_overall_average_route():
    student_name = request.form['student_name']
    student_found = False

    for student in students_data:
        if student_name.lower() == student["name"].lower():
            student_found = True
            overall_average = calculate_overall_average(student)
            result = {
                "student_name": student_name,
                "overall_average": overall_average
            }
            return jsonify(result)

    if not student_found:
        return jsonify({"message": f"No data found for the student '{student_name}'."})

@app.route('/calculate_total_students', methods=['GET'])
def calculate_total_students_route():
    total_students = len(students_data)
    result = {"total_students": total_students}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
