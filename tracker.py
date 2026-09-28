from task import Task
import json

class Tracker:
    
    def __init__(self):
        self._tasklist = []
        
    def add_task(self):
        task_name = input("Name of task: ")
        task_time = input("Time: ")
        new_task = Task(task_name, task_time, False)
        self._tasklist.append(new_task)
        
    def edit_task(self):
        if len(self._tasklist) == 0:
            print("There are no tasks to edit")
            return
        
        print("Which task to edit: ")
        for i, task in enumerate(self._tasklist):
            print(f"{i}. {task.name}")
        task_choice = input()
        try:
            task_choice = int(task_choice)
            if task_choice < 0 or task_choice > (len(self._tasklist)):
                raise ValueError
            new_name = input("New Name:    (If same name, press enter): ")
            if new_name != "":
                self._tasklist[task_choice].name = new_name
            new_time = input("New Time:    (If same time, press enter): ")
            if new_time != "":
                self._tasklist[task_choice].time = new_time
            new_status = input("Status:    (If unchanged, press enter): ")
            if new_status != "":
                self._tasklist[task_choice].status = new_status
            print(f"Edited Task: {self._tasklist[task_choice]}")
        except:
            print("Must be a valid choice")
        finally:
            return
        
    def delete_task(self):
        if len(self._tasklist) == 0:
                print("There are no tasks to edit")
                return
            
        for i, task in enumerate(self._tasklist):
            print(f"{i}. {task.name}")
        choice = input()
        
        try:
            choice = int(choice)
            if choice < 0 or choice > (len(self._tasklist)):
                    raise ValueError
            print(f"Task: {self._tasklist[choice].name} was removed")
            self._tasklist.pop(choice)
        except:
            print("Must be a valid choice")
    
    def save_list(self):
        
        try:
            with open("save.json", "x") as file:
                json_list = []
                for task in self._tasklist:
                    curr_task = task.to_dict()
                    json_list.append(curr_task)
                json.dump(json_list, file, indent = 4)
            print("Tasks save to file 'save.json'")
        except:
            print("file already exists, need to overwrite file")
    
    def load_list(self):
        try:
            with open("save.json") as file:
                saved_list = json.load(file)
                for task in saved_list:
                    curr_task = Task(task["name"], task["time"], task["status"])
                    self._tasklist.append(curr_task)
                print("Tasks loaded into task tracker")
        except Exception as error :
            print(f"An error has occured: {error}")
            
    def menu(self):
        while True:
                print("Task Tracker")
                print("1. Add new task\n2. Show current tasks\n3. Edit a task\n4. Remove a task\n5. Save Tasks\n6. Load Tasks from file\n7. Exit")
                choice = input()
                try:
                    selection = int(choice)
                    if selection < 1 or selection > 7:
                        raise ValueError
                    match selection:
                        case 1:
                            self.add_task()
                        case 2:
                            for task in self._tasklist:
                                print(f"{task}")
                            print("\n")
                        case 3:
                            self.edit_task()
                        case 4:
                            self.delete_task()
                        case 5:
                            self.save_list()
                        case 6:
                            self.load_list()
                        case 7:
                            return
                            
                except ValueError:
                    print("Must enter a valid option")