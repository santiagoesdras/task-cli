import os
import time

dbTasks = ["test","learning python"]

# add new task in array
def addTask(task):
  dbTasks.append(task)

# list the tasks in the array
def listTask():
  for task in dbTasks:
    print("* ", task)

# remove task in the array
def removeTask(i):
  i + 1
  dbTasks.pop(i)

# edit task in the array
def editTask(i, updateTask):
  i + 1
  dbTasks[i] = updateTask 

def menu(option):
  if option == "0":
    quit()

  elif option == "1":
    taskInput = input("\n\tTitle for new task: ")
    addTask(taskInput)
    
  elif option == "2":
    listTask()
   
  elif option == "3":
    try:
      removeInput = input("\n\tWhat task do you want to delete?: ")
      removeTask(int(removeInput))
    except:
      print("\tNot a number")
  
  elif option == "4":
    try:
      editInput = input("\n\tWhat task do you want to update?: ")
      updateInput = input("\n\tWhat title will you put it?: ")
      editTask(int(editInput), updateInput)
    except: 
      print("\tNot a number")

  elif option == "5":
    print("\n\tTotal tasks: ", len(dbTasks))

  else:
    print("\tOption not valid")


def imenu():
    print("\n\tOptions for you task: \n\t0.Exit \n\t1.Add new Task \n\t2.List tasks \n\t3.Delete tasks \n\t4.Update tasks \n\t5.Total tasks")

    menuOption = input("\tEnter an option ")
    menu(menuOption)

while(1):
  imenu()
  time.sleep(2)
  try:
    os.system("cls")
  except:
    os.system("clear")
 
