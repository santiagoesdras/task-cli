dbTasks = []

def addTask(task):
  dbTask.append(task)

def listTask():
  for task in dbTasks:
    print(task)

taskInput = input("Title for new task: ")

addTask(taskInput)

listTask()

