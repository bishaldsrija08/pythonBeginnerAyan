import matplotlib.pyplot as plt
grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 90,
    'Diana': 88,
    'Ethan': 95
}

# Extract names and scores
names = list(grades.keys())
scores = list(grades.values())

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(names, scores, color='skyblue')
plt.xlabel('Students')
plt.ylabel('Grades')
plt.title('Student Grades')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()