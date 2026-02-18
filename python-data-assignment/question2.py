# Create contact book dictionary
contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Tanuj": "9988776655"
}

# Print all contacts
print("Contact Book:")
for name, number in contacts.items():
    print(name, ":", number)

# Take user input
search_name = input("\nEnter name to search: ")

# Dictionary lookup using 'in'
if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")
