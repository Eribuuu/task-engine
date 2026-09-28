from datetime import time

def parse_due(value: str):
        time_components = value.split(':')
        due = time(int(time_components[0]), int(time_components[1]))
        return due