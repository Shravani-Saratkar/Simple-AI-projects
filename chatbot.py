# todo_list.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Add a new task to the list"""
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def delete_task(self, task_number):
        """Delete a task from the list"""
        try:
            del self.tasks[task_number - 1]
            print("Task deleted successfully")
        except IndexError:
            print("Invalid task number")

    def display_tasks(self):
        """Display the list of tasks"""
        print("To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. {task.description} - {status}")

    def mark_task_complete(self, task_number):
        """Mark a task as complete"""
        try:
            self.tasks[task_number - 1].completed = True
            print("Task marked as complete")
        except IndexError:
            print("Invalid task number")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Display tasks")
        print("4. Mark task complete")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            task_number = int(input("Enter task number to mark complete: "))
            todo_list.mark_task_complete(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()