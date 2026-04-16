import csv   # Import csv module

# First loop: find highest marks
with open("students2.csv", "r") as file:   # Open file in read mode
    reader = csv.reader(file)   # Read CSV file normally (not as dictionary)

    top_marks = 0   # Variable to store highest marks

    for row in reader:   # Loop through each row
        marks = int(row[3])   # Marks is in column index 3
        if marks > top_marks:   # Check if current marks are greater
            top_marks = marks   # Update highest marks

# Second loop → print Grade A, count students, find topper name
with open("students2.csv", "r") as file:   # Open file again
    reader = csv.reader(file)   # Read file again

    count = 0   # Variable to count total students

    print("Students with Grade A:")

    for row in reader:   # Loop through each row
        count += 1   # Increase total student count

        if row[4] == "A":   # Grade is in column index 4
            print(row[1])   # Name is in column index 1

        if int(row[3]) == top_marks:   # Check if marks match highest marks
            top_student = row[1]   # Store topper name

print("Total number of students:", count)   # Print total number of students
print("Student with highest marks:", top_student)   # Print topper name