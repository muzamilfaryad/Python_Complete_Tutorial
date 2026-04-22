import csv

total = 0
count = 0

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        marks = int(row["Marks"])
        total += marks
        count += 1

average = total / count

print("Average Marks:", average)