dbTasks = ["test", "learning python"]

def addTask(task):
  dbTasks.append(task)

def listTask():
  for task in dbTasks:
    print("* ", task)

def removeTask(i):
  dbTasks.pop(i)

def menu(option):
  if option == "1":
    taskInput = input("Title for new task: ")
    addTask(taskInput)

  elif option == "2":
    listTask()

print("Options for you task: \n 1. Add new Task \n 2. List tasks")

menuOption = input("Ingrese una opcion ")

menu(menuOption)

