#Zhien Luo
#1/18/2024

#init
ToDo = []
#Menu
print("Welcome to the Homework To-Do List!""Would you like to \n1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list\n5. Remove all tasks from the to-do list\n6. Sort the list alphabetically\n7. Print the number of Items on the To-do List\n8. Exit the program")
def menu():
    if i == 1:
        add= input("What homework would you like to add?")
        ToDo.append(add)
    elif i == 2:
        print("Current Schedule:")
        print(ToDo)
    elif i == 3:
        complete = int((input("Which task did you finish? (Type the # starting from 0 in order)")))
        taskname = ((input("What's the task name?")))
        ToDo[complete] = taskname + "✅"
    elif i == 4:
        delete = input(print("What task would you like to remove?"))
        ToDo.remove(delete)
    elif i == 5:
        ToDo.clear()
    elif i == 6:
        ToDo.sort()
    elif i == 7:
        c = len(ToDo)
        print("You have this amount of items in your list: " + str(c))
while True:
    i = int(input("option"))
    menu()
    if i ==8:
        break