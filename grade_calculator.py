def assign_grade(average):
    """Assigns a grade based on the average marks."""
    if average > 90:
        return 'A+'
    elif average > 80:
        return 'A'
    elif average > 70:
        return 'B'
    elif average > 60:
        return 'C'
    elif average > 50:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to process student data and generate the marks summary.
    """
    students_data = [
        {'name': 'Ravi Sharma', 'marks': [85, 92, 78]},
        {'name': 'Priya Singh', 'marks': [95, 88, 91]},
        {'name': 'Amit Patel', 'marks': [65, 72, 68]},
        {'name': 'Sneha Verma', 'marks': [55, 60, 58]},
        {'name': 'Mohan Kumar', 'marks': [45, 50, 48]}
    ]

    total_students = len(students_data)
    sum_of_all_averages = 0
    class_topper = {'name': '', 'total_marks': -1} 

    print("---------------------------------------------")
    print("        Student Marks and Grade Summary      ")
    print("---------------------------------------------")

    for student in students_data:
        student_name = student['name']
        marks = student['marks']

        total_marks = sum(marks)
        average_marks = total_marks / len(marks)

        grade = assign_grade(average_marks)

        student['total'] = total_marks
        student['average'] = average_marks
        student['grade'] = grade

        print(f"Student: {student_name}")
        print(f"  - Marks: {marks}")
        print(f"  - Total: {total_marks}")
        print(f"  - Average: {average_marks:.2f}")
        print(f"  - Grade: {grade}")
        print("-" * 25)

        
        sum_of_all_averages += average_marks

       
        if total_marks > class_topper['total_marks']:
            class_topper['name'] = student_name
            class_topper['total_marks'] = total_marks

    class_average = sum_of_all_averages / total_students

    print("\n---------------------------------------------")
    print("              Class Summary              ")
    print("---------------------------------------------")
    print(f"Total Number of Students: {total_students}")
    print(f"Class Average Score: {class_average:.2f}")
    print(f"Class Topper: {class_topper['name']} with Total Marks: {class_topper['total_marks']}")
    print("---------------------------------------------\n")

if __name__ == "__main__":
    main()