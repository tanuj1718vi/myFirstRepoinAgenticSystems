# Store employee details in a tuple
employee = (101, "Tanuj", "IT")

# Store employee roles in a set
roles = {"editor", "viewer", "admin"}

# Print employee info using tuple indexing
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

# Check admin access using set membership
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
