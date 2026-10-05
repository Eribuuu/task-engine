This weeks tasks: Simple CLI To-do list

9/16/2026:
Got the basic CRUD functionality done for the task tracker
Able to add, read, update, delete tasks
What needs to get done:
- Move tracker logic to its own class/file
- Create persistant storage for application

9/17/2026
Moved the tracker logic to its seperate file
Implemented a save function that saves to file (makes each task a json)
What needs to get done:
- fix save function (want to add a method to turn a task into a dictionary for json dumps)
- need to fix loads function
- Get all basic functiionality then focus on data typing and check edge cases
- after will write tests

9/18/2026
Didn't get too much done
Add validation into Name and Status
What needs to be done:
- Add validation in object layer for time and define time format
- Test that validation works for each attribute
- Write Tests with pytest for task and tracker methods
- Once that is done, move to FastAPI

9/24/2026
The task tracker is in an even worse state lol
I want to move on to the FastAPI portion but need to have a solid base
Going to fix the time sitaution with adding validation
Need to refactor CLI portion as well to have everything running right
Going to change time to date time for future's sake. (Actually need to wonder if thats in scope at the moment)
What needs to be done:
- Write Tests
- Make from_dict a @classmethod

9/25/2026
Task tracker is coming back alive
Base is being built steadily
Time is fixed, base domain validation is basically done
Wrote tests for setters and getters of each attribute
Note: When writing tests, write 1 happy path and then write tests for every conditional
What needs to be done:
- Make sure parse_due is working correctly as well
- Write test for parse due
- Figure out file structure of the project
- Once tests are all written, will make commit
- If all tests pass, moving to FastAPI phase
- Will worry about CLI later, maybe a different UI path when I get the web portion done

9/28/2026
Added a task id to the task class
Made a repo for this on github
Made another commit
In a semi working state, still fragile with inputs
What needs to be done:
- Write tests for task_id
- Need to fix from_dict
- Need to handle bad input for task id
- Need to add type hints 