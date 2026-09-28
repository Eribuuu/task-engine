from task import Task, Status
from datetime import datetime, time
import json

class Tracker:
    
    def __init__(self):
        self._tasklist = []
        
    def add_task(self):
        task_name = input("Name of task: ")
        print("Time: ")
        time_hour = input("Hour: ")
        time_minute = input("Minute: " )
        new_task = Task(task_name, self.set_due(int(time_hour), int(time_minute)), Status.TODO)
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
            new_due = input("New Due Time:    (If same time, press enter): ")
            if new_due != "":
                self._tasklist[task_choice].due = self.set_due(*map(int, new_due.split(":")))
            self._tasklist[task_choice].status = self.set_status()
            
            print(f"Edited Task: {self._tasklist[task_choice]}")
        except ValueError:
            print("Must be a valid choice")
        except TypeError:
            print("Must be a valid time")
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
                    curr_task = Task(task["name"], task["time"], Status(task["status"]))
                    self._tasklist.append(curr_task)
                print("Tasks loaded into task tracker")
        except Exception as error :
            print(f"An error has occured: {error}")
            
    def set_status(self):
        print("Statuses:\n1. To-Do\n2. In-Progress\n3. Done")
        selection = input()
        valid_choice = False
        status = {1: Status.TODO, 2: Status.IN_PROGRESS, 3: Status.DONE}
        while valid_choice is False:
            try:
                int_selection = int(selection)
                if int_selection < 1 or int_selection > 3:
                    raise ValueError("Must be a valid choice")
                valid_choice = True
                return status[int_selection]
            except ValueError as e:
                print(e)
                
    def set_due(self, hour, minute) -> time:
        new_time = time(hour, minute)
        return new_time
                    
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