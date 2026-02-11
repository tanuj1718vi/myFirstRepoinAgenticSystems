user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
active_input = input("Are you an active user? (True/False): ")

is_active_user = active_input == "True"

print(f"User {user_name} is {user_age} years old. Active status: {is_active_user}")
