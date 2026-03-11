def add_tasks(tasks):

    n=int(input("enter how many task you want to add:"))
    for i in range(n):
        task=input(f"Enter task{i+1}:")
        tasks.append(task)

def show_tasks(tasks):
    print("\n Your task:")
    if len(tasks)==0 :
       print("no task avilable.")
    else:
     for i in range(len(tasks)):
        print(f"{i+1} . {tasks[i]}")

def delete_tasks(tasks):
    choice= input("\ndo you want to delete task?(yes/no): ").lower()
    

    if choice=="yes":
        show_tasks(tasks)
        try:
            task_number= int(input("\nWhich task number do you want to delete?:"))
       
            if  1 <= task_number <= len(tasks):
             del tasks[task_number - 1]
             print("\nTask deleted successfully!")
            else:
             print("\nInvalid task number!")

        except ValueError:
            print("\nPlease enter a valid number!")
    elif choice=="no":
        print("\nNo task deleted.") 
    else:
       print("\nInvalid choice! Please type 'yes' or 'no'.")
    
    print("\nUpdated task list:")
    show_tasks(tasks)

task_list=[]  

while True: 
   
   add_tasks(task_list)
   show_tasks(task_list)
   delete_tasks(task_list)  

   more=input("\ndo you want to add more task?(yes/no): ").lower()

   if more !="yes":
    print("\nFinal tasks List:")
    show_tasks(task_list)
    print("program ended")
    break
