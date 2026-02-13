# Sum Until Zero

total = 0

while True:
    number = int(input("Enter number: "))
    
    if number == 0:
        break
    
    total += number

print("Total:", total)
