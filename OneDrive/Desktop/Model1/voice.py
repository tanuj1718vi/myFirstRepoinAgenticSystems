import speech_recognition as sr


def voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak your task...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
    except sr.RequestError:
        print("Internet error.")

    return None


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task_keyboard(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully!")


def add_task_voice(tasks):
    task = voice_input()
    if task:
        tasks.append(task)
        print("Voice task added successfully!")


def show_tasks(tasks):
    print("\n----- YOUR TASKS -----")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("----------------------\n")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"'{removed_task}' deleted successfully!")
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
            add_task_keyboard(tasks)
            save_tasks(tasks)

        elif choice == "2":
            add_task_voice(tasks)
            save_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)

        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()