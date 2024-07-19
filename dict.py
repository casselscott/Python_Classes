# Step 1: Create the dictionary
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Step 2: Add a new student and grade
students["David"] = 88

# Step 3: Modify the grade of an existing student
students["Alice"] = 90

# Step 4: Remove a student from the dictionary
del students["Charlie"]

# Step 5: Print all student names and their grades
for name, grade in students.items():
    print(f"Student: {name}, Grade: {grade}")
