# Store marks of at least 8 students
marks = [78, 85, 92, 67, 88, 74, 90, 81]

# Print full list
print("All Marks:", marks)

# Print first 3 marks
print("First 3 Marks:", marks[:3])

# Print last 3 marks
print("Last 3 Marks:", marks[-3:])

# Calculate highest, lowest, and average
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Mark:", round(average, 2))
  