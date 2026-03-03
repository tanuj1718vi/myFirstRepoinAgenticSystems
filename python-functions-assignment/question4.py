# Function 1: Greeting
def greet_student(name):
    return f"Hello, {name}! Here is your performance report."


# Function 2: Calculate stats
def calculate_stats(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score


# Function 3: Determine result
def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Main function
def main():
    name = "Tanuj"
    scores = [65, 72, 48, 80, 55]

    greeting = greet_student(name)
    subjects, average = calculate_stats(scores)
    result = evaluate_result(average)

    print(greeting)
    print("Number of Subjects:", subjects)
    print("Average Score:", round(average, 2))
    print("Final Result:", result)


# Run the program
main()
