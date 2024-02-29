#functions to display data
def display_subject_statistics(subject, average, highest, lowest):
    print(f"\nStatistics for {subject}:")
    print(f"  Average Grade: {average:.2f}")
    print(f"  Highest Grade: {highest}")
    print(f"  Lowest Grade: {lowest}")

def display_overall_average(student_name, overall_average):
    print(f"\nOverall Average Grade for {student_name}: {overall_average:.2f}")