import speech_recognition as sr

def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak your task...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
    except sr.RequestError:
        print("Internet error.")
    
    return None
def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_tasks(tasks):
    while True:
        try:
            n = int(input("How many tasks do you want to add? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(n):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)

    print("Tasks added successfully!")


def show_tasks(tasks):
    print("\n===== YOUR TASKS =====")
    if not tasks:
        print("No tasks available.")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    print("======================\n")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks(tasks)

    while True:
        try:
            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"'{removed}' deleted successfully!")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("====== TASK MANAGER ======")
        print("1. Add Task (Keyboard)")
        print("2. Add Task (Voice)")
        print("3. Show Tasks")
        print("4. Delete Task")
        print("5. Exit") 
        print("==========================")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_tasks(tasks)
            save_tasks(tasks)

        elif choice == "2":
         task = voice_input()
         if task:
          tasks.append(task)
          save_tasks(tasks)
          print("Voice task added successfully!" )

        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)

        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break

        else:
            print("Invalid choice. Please select 1-4.")


# Run Program
if __name__ == "__main__":
    main()