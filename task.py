class Task:
    def __init__(self, name, time, status = False):
        self.name = name
        self.time = time
        self.status = status
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, value):
        self._time = value
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value
        
    def __str__(self) -> str:
        return f"Name: {self.name}| Do at: {self.time}| Status: {self.status}"
    
    def to_dict(self):
        task_dict = {"name" : self.name, "time": self.time, "status": self.status}
        return task_dict
    