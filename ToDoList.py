

#Add Task
def add_task():
    New_task=input('Enter a New Task :')
    TodoList.append({'Task':New_task,'status':'Pending'})
    #To write a todolist in text file
    with open("ToDoList.txt",'w') as FileWrite:
        for index,data in enumerate(TodoList,1):
            FileWrite.writelines(f'{index}.{str(data['Task'])} - {str(data['status'])}\n')
    print('New Task Added\n')

#View Task
def View_Task():
    if len(TodoList)==0:
        print('Nothing to view\n')
    else:
        for index,tsk in enumerate(TodoList,1):
            print(f'{index} : {tsk['Task']} - {tsk['status']}')
#Mark Task
def Mark_Task():
    if len(TodoList)==0:
        print('Nothing to Mark in the ToDoList')
    else:
        search=int(input('Which one you want to Mark as Complete :'))-1
        try:
            if 0<=search<len(TodoList):
                TodoList[search]['status']='Completed'
                #To write a todolist in text file
                with open("ToDoList.txt",'w') as FileWrite:
                    for index,data in enumerate(TodoList,1):
                        FileWrite.writelines(f'{index}.{str(data['Task'])} - {str(data['status'])}\n')
                print(f'The {TodoList[search]['Task']} is Mark as Completed')
            else:
                print('Invalid Choices in the TodoList')
        except Exception:
            print('Invalid Mark in the TodoList')
#remove task
def remove_task():
    if len(TodoList)==0:
        print('Nothing to remove in the ToDoList Task')
    else:
        search=int(input('Which one you want to Remove from the ToDoList :'))-1
        try:
            if 0<=search<len(TodoList):
                remove=TodoList.pop(search)
                print(f'The task {remove['Task']} successfully')
        except ValueError:
            print('Invalid TodoList to Remove')

#Define as list
TodoList=[]

#Create a main menu
while True:
    print('Todo List Menu:')
    print('1. Add New Task')
    print('2. View a Task')
    print('3  Mark a Task as Completed')
    print('4. Remove a Task')
    print('5. Exit')

    Choice = input('Enter a choice from the above Task : ')
    if Choice=='1':
        add_task()
    elif Choice=='2':
        View_Task()
    elif Choice=='3':
        Mark_Task()
    elif Choice=='4':
        remove_task()
    elif Choice=='5':
        print('Exiting the application')
        exit()
    else:
        print('Invalid Task \n')
           