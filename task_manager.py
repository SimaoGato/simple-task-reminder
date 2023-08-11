tasks = [];

def showMenu():
    print("1. Add task.\n2. Remove task.\n3. Show tasks.\n4. Exit.")

def addTask():
    print("Enter task: ");
    task = input();
    print("Enter due date: ");
    dueDate = input();
    task = { "task": task, "dueDate": dueDate };
    tasks.append(task);
    print("Task added.");

def removeTask():
    print("Enter task name: ");
    task = input();
    for i in range(len(tasks)):
        if tasks[i]["task"] == task:
            tasks.pop(i);
            print("Task removed.");
            break;

def showTasks():
    for i in range(len(tasks)):
        print(tasks[i]["task"] + " - " + tasks[i]["dueDate"]);

if __name__ == "__main__":
    while True:
        showMenu();
        option = int(input());
        if option == 1:
            addTask();
        elif option == 2:
            removeTask();
        elif option == 3:
            showTasks();
        elif option == 4:
            break;
        else:
            print("Invalid option.");
