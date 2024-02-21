from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # create an instance of the SQLAlchemy object. This db object represents the database and will be used to interact with the database.

class Task(db.Model): # create a class that maps to the database table. This class inherits from db.Model. This class represents a table in the database.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    dueDate = db.Column(db.String(10))
    status = db.Column(db.String(10))
    #4 why is db not defined.. does it need to be imported?

    def __init__(self, title, description, dueDate, status):
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.status = status

    def update_status(self, new_status):
        self.status = new_status
        print(f"Task {self.title} has been updated to {new_status}")
    
class TodoList:
    def __init__(self):
        # attributes
        self.todo_list = [] # this attribute acts as container for tasks - its the actual list that stores instance of Task objects

    # methods: mainpulates a certain instance 
    def add_todo(self, title, description, dueDate, status):
        new_todo = Task(title, description, dueDate, status)
        self.todo_list.append(new_todo)

    def delete_todo(self, title):
        for i, task in enumerate(self.todo_list):
            if task.title == title:
                del self.todo_list[i]
                print(f"Todo item '{title}' has been removed.")
                return
        print("No item found")

"""    def display_tasks(self):
        if not self.todo_list:
            print("No tasks to display.")
            return
        for i, task in enumerate(self.todo_list, start=1):
            print(f"Task {i}: {task.title}")
            print(f"  Description: {task.description}")
            print(f"  Due Date: {task.dueDate}")
            print(f"  Status: {task.status}")
            print("")"""