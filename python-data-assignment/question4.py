# Function to calculate average score of each user
def calculate_average(users):
    averages = []

    for user in users:
        scores = user["scores"]
        average = sum(scores) / len(scores)
        averages.append((user["name"], average))  # storing as tuple

    return averages


# Function to check admin access
def has_admin_access(roles):
    return "admin" in roles


# Main function
def main():
    # List of users (each user is a dictionary)
    users = [
        {
            "name": "Alice",
            "scores": [85, 78, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [60, 70, 65],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [95, 88, 92],
            "roles": {"editor", "viewer"}
        }
    ]

    # Calculate averages
    averages = calculate_average(users)

    # Print results
    for user in users:
        name = user["name"]
        roles = user["roles"]

        # Get average from tuple list
        for avg_data in averages:
            if avg_data[0] == name:
                average_score = avg_data[1]

        print("Name:", name)
        print("Average Score:", round(average_score, 2))
        print("Admin Access:", has_admin_access(roles))
        print("-" * 30)


# Run program
main()
