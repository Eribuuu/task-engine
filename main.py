from tracker import Tracker
from task import Task, Status
from datetime import time

def main():
    test_task = Task("Laundry", time(12, 30))
    task_dict = test_task.to_dict()
    print(task_dict)
    
if __name__ == "__main__":
    main()