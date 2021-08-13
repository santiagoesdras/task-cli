from tabulate import tabulate, tabulate_formats
from sys import platform
import os

dbTasks = []
options = ["0.Exit" , "1.Add new Task", "2.Delete tasks" , "3.Update tasks"]

# add new task in array
def addTask(task):
  dbTasks.append(task)

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
    taskInput = input("\n\tTitle for new task: ")
    addTask(taskInput)
    
  elif option == "2":
    try:
      removeInput = input("\n\tWhat task do you want to delete?: ")
      removeTask(int(removeInput))
    except:
      print("\tNot a number")
   
  elif option == "3":
    try:
      editInput = input("\n\tWhat task do you want to update?: ")
      updateInput = input("\n\tWhat title will you put it?: ")
      editTask(int(editInput), updateInput)
    except: 
      print("\tNot a number")
  else:
    print("\tOption not valid")

def printlists():
  task = dbTasks
  print(tabulate({"Tasks" : task, "Options" : options}, headers = "keys"))
  menuOption = input("\tEnter an option ")
  menu(menuOption)


while(1):
  if platform == "win32": 
    os.system("cls")
  else:
    os.system("clear")
  printlists()

