import matplotlib.pyplot as plt
import csv

subjects = []
marks = []

with open("marks.csv") as file:
    reader = csv.reader(file)
    next(reader)   # skip header

    for row in reader:
        subjects.append(row[0])
        marks.append(int(row[1]))

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks by Subject")

plt.show()