# Secure Transaction Validator

balance = int(input("Balance: "))
withdrawal = int(input("Withdrawal: "))
verified_input = input("Verified (True/False): ").lower()

if verified_input == "true":
    verified = True
elif verified_input == "false":
    verified = False
else:
    print("Invalid verification input")
    exit()

# Compound Boolean condition
if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
