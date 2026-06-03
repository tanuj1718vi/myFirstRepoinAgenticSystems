def getting():
 number=[]
 try:
   n=int(input("How many numbers you want to enter:"))
 except ValueError:
   print("invalid input")
   n=0
 for i in range (n):
    try:
        num=(int(input(f"enter your number {i+1}:")))
        number.append(num)

    except ValueError:
      print("invalid input")
 return number
def calculate(number):
 if len(number)>0:
  print("sum",sum(number))
  print("min",min(number))
  print("max",max(number))
  print("average",sum(number)/len(number))
  print("sorted",sorted(number))

 else:
  print("invalid input values")
num=getting()
calculate(num)