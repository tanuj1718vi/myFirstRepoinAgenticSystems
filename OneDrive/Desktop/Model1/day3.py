# number= int(input("enter a number"))

# if number>0 :
#   print("positive")
# elif number<0 :
#   print("negetive")
# else :
#   print("zero")
# if number%2 ==0 :
#  print("even")
# else :
#   print("odd")
number=[]
for i in range (5):
    try:
        num=(int(input(f"Enter your number{i+1}:")))
        number.append(num)
    except:
      print("You enter a invalid number")   
Largest=-9999
Second_largest=-9999
for num in number :
    if num > Largest:
       Second_largest=Largest
       Largest=num
    elif num > Second_largest and num !=Largest :
        Second_largest=num
print("Largest",Largest)
print("Second largest",Second_largest)
