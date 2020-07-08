#Written by Logan Jakuboski
#This program manages tasks for the user

import json
import datetime

#This is the main function for the program
def main():

    manage_tasks = True
    tasks = load_tasks()

    print('----------------------------')
    print('Welcome to the Task Manager!')
    print('----------------------------')
    
    while(manage_tasks):
        show_menu()
        while(True):
            try:
                choice = int(input('What would you like to do? '))
                if(choice < 1 or choice > 5):
                    print(choice, 'is not a valid choice.')
                    continue
            except ValueError:
                print('The value you entered is invalid. Only numerical values are valid.')
            else:
                break
        if(choice == 1):
            create_task(tasks)
        elif(choice == 2):
            show_tasks(tasks)
        elif(choice == 3):
            edit_task(tasks)
        elif(choice == 4):
            delete_task(tasks)
        elif(choice == 5):
            manage_tasks = False


#This function prints the menu to the user
def show_menu():
    print('')
    print('---------')
    print('TASK MENU')
    print('---------')
    print("1. Create a task")
    print("2. View previous tasks")
    print("3. Edit a task")
    print("4. Delete a task")
    print("5. Quit")

#This function takes in the tasks dictionary and creates a new task
def create_task(tasks):
    print('')
    while(True):
        validation = True
        try:
            name = input(str('Name of Task: '))
            for task in tasks:
                if(name == task):
                    print('Task already exists!')
                    validation = False
            if(validation == False):
                continue
        except NameError:
            print('Task already exists!')
        else:
            break
    description = input(str('Description: '))
    location = input(str('Location: '))
    isValidDate = True
    while(isValidDate):
        try:
            date = input(str("Enter Due date 'mm/dd/yy': "))
            month,day,year = date.split('/')
            datetime.datetime(int(year),int(month),int(day))
        except ValueError:
            print('Date is not valid')
        else:
            break
        

    task = { name : {
        'Description' : description,
        'Location' : location,
        'Due' : date
    }}
    tasks.update(task)
    write_to_file(tasks)
        

#This function takes in the tasks dictionary and prints them to the user
def show_tasks(tasks):
    if not tasks:
        print('No tasks exist!')
    else:
        print('')
        for task in tasks:
            print('Name:', task)
            print('Description:', tasks[task]['Description'])
            print('Location:', tasks[task]['Location'])
            print('Due:', tasks[task]['Due'])

#This function loads the tasks dictionary from a json file and creates a new one if it doesn't exist
def load_tasks():
    try:
        file = open('tasks.json', 'r')
        data = json.load(file)
        tasks = {}
        tasks.update(data)
        file.close()
    except :
        tasks = {}
    return tasks

#This function writes the tasks dictionary to the json file
def write_to_file(task):
    task_json = json.dumps(task, indent=3)
    try:
        file = open('tasks.json', "w")
        file.write(task_json)
        file.close()
    except :
        print('Unable to write to file');

#This function searches through tasks and deletes if it exists
def delete_task(tasks):
    if not tasks:
        print('No tasks exist!')
    else:
        print('')
        name = input(str('Enter task name: '))
        if name in tasks:
            del tasks[name]
            write_to_file(tasks)
        else:
            print("Task doesn't exist!")

#This function allows the user to edit a task
def edit_task(tasks):
    if not tasks:
        print('No tasks exist!')
    else:
        print('')
        name = input(str('Enter task name: '))
        if name in tasks:
            edit_choices(name, tasks)
            while(True):
                repeat = input('Would you like to edit more values? (y/n):')
                if(repeat != "y"):
                    break
                edit_choices(name, tasks)
            
            write_to_file(tasks)
        else:
            print("Task doesn't exist!")

#This function provides a menu for the user and allows them to change a value in a task
#This takes in the tasks dictionary and the name of the task that is editing 
def edit_choices(name, tasks):
    while(True):
        print("Current Values")
        print("--------------")
        print('1. Description:', tasks[name]['Description'])
        print('2. Location:', tasks[name]['Location'])
        print('3. Due:', tasks[name]['Due'])
        print('4. Cancel')
        try:
            choice = int(input('What would you like to edit? '))
            if(choice < 1 or choice > 4):
                print(choice, 'is not a valid choice.')
                continue
        except ValueError:
            print('The value you entered is invalid. Only numerical values are valid.')
        else:
            break
    if(choice == 1):
        description = input(str('Description: '))
        newTask = { name : {
            'Description' : description,
            'Location' : tasks[name]['Location'],
            'Due' : tasks[name]['Due']
        }}
        tasks.update(newTask)
        show_edits(name, tasks)
    elif(choice == 2):
        location = input(str('Location: '))
        newTask = { name : {
            'Description' : tasks[name]['Description'],
            'Location' : location,
            'Due' : tasks[name]['Due']
        }}
        tasks.update(newTask)
        show_edits(name, tasks)
    elif(choice == 3):
        isValidDate = True
        while(isValidDate):
            try:
                date = input(str("Enter Due date 'mm/dd/yy': "))
                month,day,year = date.split('/')
                datetime.datetime(int(year),int(month),int(day))
            except ValueError:
                print('Date is not valid')
            else:
                break
        newTask = { name : {
            'Description' : tasks[name]['Description'],
            'Location' : tasks[name]['Location'],
            'Due' : date
        }}
        tasks.update(newTask)
        show_edits(name, tasks)
    elif(choice == 4):
        print('No Action Detected!')

#This function shows the edits after changing values      
def show_edits(name, tasks):
    print("New Values")
    print("--------------")
    print('1. Description:', tasks[name]['Description'])
    print('2. Location:', tasks[name]['Location'])
    print('3. Due:', tasks[name]['Due'])
  
main()
