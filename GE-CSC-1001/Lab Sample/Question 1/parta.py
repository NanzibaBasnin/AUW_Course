import csv

with open("students2.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["StudentID", "Name", "Subject", "Marks", "Grade"])

    for i in range(8):
        student_id = input("Enter Student ID (e.g., S001): ").strip()
        name = input("Enter Name: ").strip()
        subject = input("Enter Subject: ").strip()
        marks = int(input("Enter Marks: "))
        grade = input("Enter Grade (A/B/C/F): ").strip().upper()

        writer.writerow({
            "StudentID": student_id,
            "Name": name,
            "Subject": subject,
            "Marks": marks,
            "Grade": grade
        })