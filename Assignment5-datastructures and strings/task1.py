# Step 1: Create a dictionary with student names and marks
student_marks = {
    "Ash": 85,
    "sam": 78,
    "vin": 92,
    "Dan": 88,
    "alphasam": 95
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the marks, handling missing names
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in records.")
