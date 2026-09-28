from enum import StrEnum
from datetime import time
from serialization import parse_due

class Status(StrEnum):
    TODO = "To-Do"
    IN_PROGRESS = "In-Progress"
    DONE = "Done"
    
class Task:
    def __init__(self, name: str, due_at, status: Status = Status.TODO):
        self.name = name
        self.due = due_at
        self.status = status
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Name of task must be a string")
        
        clean_value = value.strip()
        
        if len(clean_value) < 3:
            raise ValueError("Name must be longer than 2 characters ")
            
        self._name = clean_value
    
    @property
    def due(self):
        return self._due
    
    @due.setter
    def due(self, value):
        
        if not isinstance(value, time):
            raise TypeError("Must be of time type")
        
        self._due = value
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value: Status):
        
        if not isinstance(value, Status):
            raise TypeError("Status must be of Status type")
        
        self._status = value
        
    def __str__(self) -> str:
        return f"Name: {self.name}| Due at: {self.due}| Status: {self.status}"
    
    def to_dict(self):
        task_dict = {"name" : self.name, "due": self.due.strftime("%H:%M"), "status": self.status.value}
        return task_dict
    
    @classmethod
    def from_dict(cls, task_dict):
            name = task_dict["name"]
            due = parse_due(task_dict["due"])
            status = Status(task_dict["status"])
            return cls(name, due, status)
