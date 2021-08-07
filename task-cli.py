dbTasks = ["test", "learning python"]

# add new task in array
def addTask(task):
  dbTasks.append(task)

# list the tasks in the array
def listTask():
  dbTasks.reverse()
  for task in dbTasks:
    print("* ", task)

# remove task in the array
def removeTask(i):
  dbTasks.pop(i)

# edit task in the array
def editTask(i, updateTask):
  dbTasks[i] = updateTask 

def menu(option):
  if option == "0":
    quit()

  elif option == "1":
    taskInput = input("Title for new task: ")
    addTask(taskInput)

  elif option == "2":
    listTask()

  elif option == "3":
    try:
      removeInput = input("What task do you want to delete?: ")
      removeTask(int(removeInput))
    except:
      print("Not a number")
  
  elif option == "4":
    try:
      editInput = input("What task do you want to update?: ")
      updateInput = input("What title will you put it?: ")
      editTask(int(editInput), updateInput)
    except: 
      print("Not a number")

  elif option == "5":
    print("Total tasks: ", len(dbTasks))

  else:
    print("Option not valid")

while(1):
  print("Options for you task: \n 1. Add new Task \n 2. List tasks")

  menuOption = input("Ingrese una opcion ")

  menu(menuOption)

