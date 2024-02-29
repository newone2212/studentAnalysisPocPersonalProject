import os
# function for Analysis
def calculate_subject_statistics(subject_data):
    try:
        total_grades = 0
        highest_grade = float('-inf')
        lowest_grade = float('inf')
        print(subject_data)
        for grade in subject_data.values():
            print(grade)
            total_grades += grade
            highest_grade = max(highest_grade, grade)
            lowest_grade = min(lowest_grade, grade)

        average_grade = total_grades / len(subject_data)
        return average_grade, highest_grade, lowest_grade
    except TypeError as e:
        return f"Error: {e}. The 'subject_data' should be a dictionary with numeric values."
    except ZeroDivisionError as e:
        return f"Error: {e}. 'subject_data' should not be an empty dictionary."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def calculate_overall_average(student_data):
    try:
        grades = student_data["grades"]
        if not grades or not isinstance(grades, dict):
            raise ValueError("Invalid 'grades' data. It should be a non-empty dictionary.")

        total_grades = sum(grades.values())
        overall_average = total_grades / len(grades)
        return overall_average

    except ZeroDivisionError as e:
        return f"Error: {e}. The 'grades' dictionary should not be empty."
    except TypeError as e:
        return f"Error: {e}. 'grades' should be a dictionary with numeric values."
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
