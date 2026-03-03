age = int(input("Age: "))
has_id = input("Has ID (True/False): ").lower()

if has_id == "true":
    has_id = True
elif has_id == "false":
    has_id = False
else:
    print("Invalid ID input")
    exit()

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
