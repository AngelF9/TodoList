from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # create an instance of the SQLAlchemy object. This db object represents the database and will be used to interact with the database.

class Task(db.Model): # create a class that maps to the database table. This class inherits from db.Model. This class represents a table in the database.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    dueDate = db.Column(db.String(10))
    status = db.Column(db.String(10))
    important = db.Column(db.Boolean, default=False)    #4 why is db not defined.. does it need to be imported?

    def __init__(self, title, description, dueDate, status, important):
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.status = status
        self.important = important

    def __repr__(self):
        return f'<Task {self.title}>'
    

    def update_status(self, new_status):
        self.status = new_status
        print(f"Task {self.title} has been updated to {new_status}")