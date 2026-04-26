def adding(number):
    try:
        n=int(input("how many numbers you want to add "))
    except ValueError:
        print("invalid input")
        n=0
    for i in range(n):
      try:
        num=int(input(f"Enter your number {i+1} :"))
        number.append(num)
      except ValueError:
         print("Invalid input")
    return number
def save_numbers(number):
    with open("numbers.txt","w") as f:
       for num in number:
          f.write(str(num) + "\n")
def load_number():
 number = []
 try:  
  with open("numbers.txt", "r") as f:
    for line in f:
        number.append(int(line.strip()))
  return number
 except FileNotFoundError:
   return[]
def showing(number):
    print("your numbers are ",number)
def find_sum(number):
     if len(number)>0:
      print("sum of your numbers are :",sum(number))
     else:
      print("NO number avilable")
def minmax(number):
     if len(number)>0:
        print("minimum number is :",min(number))
        print("maximum number is :",max(number))
     else:
        print("NO number avilable")
def main():
   number = load_number()
   while True:
      print("====Task manager====")
      print("1. Add number:")
      print("2. Show number")
      print("3. sum")
      print("4. Min and Max")
      print("5. save data")
      print("6. Exit")
      print("=====================")
      choice =input("Choose any option (1-6) :")
      if choice=="1":
       adding(number)
       save_numbers(number)
      elif choice=="2":
       showing(number)
      elif choice=="3":
       find_sum(number)
      elif choice=="4":
       minmax(number)
      elif choice=="5":
       save_numbers(number)
       print("saved data successfully ")
      elif choice=="6":
       print("Good bye") 
       break
      else:
       print("Invalid choice")
      
      
    
#main code 
main()