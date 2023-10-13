tasks = []
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" has been added to your to-do list.')
def show_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
    else:
        print("Your to-do list is empty.")
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f'Task "{completed_task}" has been marked as completed.')
    else:
        print("Invalid task index. Please enter a valid task number.")
while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Mark a task as completed")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
