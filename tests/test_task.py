from datetime import datetime, time
from task import Task, Status
import pytest
#Test Each setter and property
#Test task
test_task = Task("Test", time(10, 30), None, Status.TODO)
#Name Getter
def test_name_getter():
    assert test_task.name == "Test" 
    
#Name setter
def test_name_setter_happy_path():
    test_task.name = "New Test"
    assert test_task.name == "New Test"

def test_name_setter_wrong_type():
    with pytest.raises(TypeError):
        test_task.name = 123

def test_name_setter_strip():
    test_task.name = "  1234   "
    assert test_task.name == "1234"
    
def test_name_setter_short_name():
    with pytest.raises(ValueError):
        test_task.name = "12"

def test_name_setter_boundary_lower():
    with pytest.raises(ValueError):
            test_task.name = "12"

def test_name_setter_boundary_upper():
    test_task.name = "123"
    assert test_task.name == "123"

#Due getter
def test_due_getter():
    check_due = time(10, 30)
    assert test_task.due == check_due

#Due setter
def test_due_happy_path():
    test_task.due = time(12, 45)
    assert test_task.due == time(12, 45)

def test_due_wrong_type():
    with pytest.raises(TypeError):
        test_task.due = 123
def test_due_datetime():
    with pytest.raises(TypeError):
        test_task.due = datetime(2002, 12, 15, 12, 45)

#Status getter
def test_status_getter():
    assert test_task.status == Status.TODO

#Status setter
def test_status_happy_path():
    test_task.status = Status.DONE
    assert test_task.status == Status.DONE
    
def test_status_wrong_type():
    with pytest.raises(TypeError):
        test_task.status = "done"

#Create Dictionary from task object
def test_to_dictionary():
    new_task = Task("Test", time(10, 30), None, Status.TODO)
    test_dict = new_task.to_dict()
    assert test_dict["name"] == "Test"
    assert test_dict["due"] == "10:30"
    assert test_dict["status"] == "To-Do"

#Create task object from dictionary
def test_from_dictionary():
    new_task = Task("Test", time(10, 30), None, Status.TODO)
    test_dict = new_task.to_dict()
    recreated_task = Task.from_dict(test_dict)
    assert recreated_task.name == new_task.name
    assert recreated_task.due == new_task.due
    assert recreated_task.status == new_task.status