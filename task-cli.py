dbTasks = ["test", "learning python"]

def booleanvalue(ciclo):
  if ciclo > 0:
    return 1
  elif ciclo <=0:
    return 0

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
    ciclo = +1
    booleanvalue(ciclo)

  elif option == "2":
    listTask()
    ciclo = +1
    booleanvalue(ciclo)

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


def imenu():
    print("\n\tOptions for you task: \n\t0.Exit \n\t1.Add new Task \n\t2.List tasks \n\t3.Delete tasks")

    menuOption = input("\tEnter an option ")
    menu(menuOption)

while(booleanvalue):
  imenu()
 
