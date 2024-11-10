import random
import csv

FILE = 'student_grades.csv'
grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'FF']
probabilities = [0.05, 0.25, 0.25, 0.25, 0.15, 0.1, 0.08, 0.02]

grades_table = []
for _ in range(10):
    row = []
    for _ in range(20):
        cur_seq = ""
        for _ in range(12):
            cur_seq += random.choices(grades, probabilities)[0]
        row.append(cur_seq)
    grades_table.append(row)

with open(FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    header = [f"Student{i+1}" for i in range(20)]
    writer.writerow(header)
    writer.writerows(grades_table)

print(f"CSV file {FILE} created successfully.")
