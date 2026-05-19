import matplotlib.pyplot as plt
import numpy as np

# Student names
students = ["AMIT", "RIYA", "JOHN"]

# Marks for different subjects
maths = [85, 92, 78]
science = [88, 90, 80]
english = [82, 95, 75]

# ---------- Simple Bar Chart ----------
plt.figure(figsize=(8,5))
plt.bar(students, maths)

plt.title("Student Marks Dashboard")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)

for i in range(len(students)):
    plt.text(i, maths[i] + 1, str(maths[i]), ha='center')

plt.show()


# ---------- Bonus: Grouped Bar Chart ----------
x = np.arange(len(students))
width = 0.25

plt.figure(figsize=(10,5))

plt.bar(x - width, maths, width, label="Maths")
plt.bar(x, science, width, label="Science")
plt.bar(x + width, english, width, label="English")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Comparison")
plt.xticks(x, students)
plt.ylim(0, 100)

plt.legend()

plt.show()