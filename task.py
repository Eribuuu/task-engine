import uuid
from enum import StrEnum
from datetime import time
from serialization import parse_due

class Status(StrEnum):
    TODO = "To-Do"
    IN_PROGRESS = "In-Progress"
    DONE = "Done"
    
class Task:
    def __init__(self, name: str, due_at, task_id = None, status: Status = Status.TODO):
        if task_id is None:
            self._task_id = uuid.uuid4()
        else:
            if not isinstance(task_id, uuid.UUID):
                raise TypeError("task_id must be of uuid type")
            self._task_id = task_id
        self.name = name
        self.due = due_at
        self.status = status
    
    @property
    def id(self):
        return self._task_id
    
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
        task_dict = {"id": str(self.id), "name" : self.name, "due": self.due.strftime("%H:%M"), "status": self.status.value}
        return task_dict
    
    @classmethod
    def from_dict(cls, task_dict):
        id = uuid.UUID(task_dict["id"])
        name = task_dict["name"]
        due = parse_due(task_dict["due"])
        status = Status(task_dict["status"])
        return cls(name, due, id, status)
