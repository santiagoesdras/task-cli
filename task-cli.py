dbTasks = ["test", "learning python"]

def booleanvalue(ciclo):
  if ciclo > 0:
    return 1
  elif ciclo <=0:
    return 0

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
    ciclo = +1
    booleanvalue(ciclo)

  elif option == "2":
    listTask()
    ciclo = +1
    booleanvalue(ciclo)

  elif option == "3":
    ciclo = 0
    booleanvalue(ciclo)

def imenu():
    print("\n\t\t\tOptions for you task: \n \t\t\t1. Add new Task \n \t\t\t2. List tasks \n \t\t\t3.Exit program")

    menuOption = input("\t\t\tEnter an option ")
    menu(menuOption)

while(booleanvalue):
  imenu()

  print('bien hecho el ciclo')
  listTask()
  




