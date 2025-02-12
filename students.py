import json

# Read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Access the list of students
students = data['students']

# Process the data
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print()  # Print a blank line for better readability