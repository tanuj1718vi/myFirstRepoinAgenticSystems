accuracy = input("Enter model accuracy: ")

if accuracy.replace(".", "", 1).isdigit():
    accuracy = float(accuracy)
    print(f"Model accuracy is {accuracy}")
else:
    print("Invalid input. Please enter a numeric value.")
