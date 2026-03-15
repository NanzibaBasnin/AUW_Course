import matplotlib.pyplot as plt
import csv

subjects = []
scores = []

with open('marks.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        subjects.append(row['Subject'])
        scores.append(int(row['Marks']))

plt.pie(scores, labels=subjects, autopct='%.2f%%')
plt.title('Marks of a Student', fontsize=20)
plt.show()