
 number=[]
 try:
   n=int(input("How many numbers you want to enter:"))
 except ValueError:
   print("invalic input")
   n=0
 for i in range (n):
    try:
        num=(int(input(f"enter your number {i+1}:")))
        number.append(num)

    except:
      print("invalid input")
 if len(number)>0:
  print(number)
  print("sum",sum(number))
  print("min",min(number))
  print("max",max(number))
  print("average",sum(number)/len(number))
  print("sorted",sorted(number))

 else:
  print("invalid values")