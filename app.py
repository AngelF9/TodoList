from flask import Flask, render_template, request, redirect, url_for, jsonify
from Task import db                             # import the db object from the Task module. db is the SQLAlchemy object that we created in Task.py
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                       # create an instance of the Flask class
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # set the database URI. This is the path to the database file. The database file will be created in the same directory as the app.py file.
db.init_app(app)                                            # initialize the db object with the app object. This binds the database to the app.

from Task import Task                                       # import the Task class from the Task module. This is the class that maps to the database table.

@app.route('/') 
def index():                                                # function generates the URL for the index route... this function renders the main page
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])            # flask is listening for POST request at this /add route
def add_task():                                 # when POST request hits route above^ the function add_task is called
    title = request.form['title']               # request.form is a dictionary that contains the data from the form
    description = request.form['description']   # ['...'] extract data from the respective fields filled out in the form
    dueDate = request.form['dueDate']
    status = request.form['status']
    important = request.form.get('important', False)
    new_task = Task(title, description, dueDate, status, important)    # create a new instance of Task
    db.session.add(new_task)                                #  add the new instance to the database session (pending/limbo state)
    db.session.commit()                                     # commit the session to the database
    return redirect(url_for('index'))           # function does not return HTML directly. instead it redirects the user back to the index route 

@app.route('/tasks')
def task():
    tasks = Task.query.all() # query the database for all tasks
    return render_template('tasks.html', tasks=tasks) # render the tasks.html template and pass the tasks to it

@app.route('/edit/<int:task_id>', methods=['GET', 'POST']) 
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)       # get the task with the given id or return 404 if not found
    if request.method == 'POST':                # if the request method is POST, update the task
        task.title = request.form['title']
        task.description = request.form['description']
        task.dueDate = request.form['dueDate']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id) # if the task_id is found the we have found the task.. else return 404
    db.session.delete(task)              # delete the task from the database session
    db.session.commit()                 # commit the session to the database
    return redirect(url_for('index'))   # redirect the user back to the index route

@app.route('/important') # function generates the URL for the important route
def view_important(): # function renders the important page
    tasks = Task.query.filter_by(important=True).all() # query the database for all tasks that are important
    return render_template('important.html', tasks=tasks) # render the important.html template and pass the tasks to it

@app.route('/update_important/<int:task_id>', methods=['POST']) # function generates the URL for the update_important route
def update_important(task_id): # function updates the important status of a task
    task = Task.query.get_or_404(task_id) # get the task with the given id or return 404 if not found
    task_data = request.json # get the JSON data from the request
    task.important = task_data.get('important', task.important) # update the important status of the task by getting the important value from the JSON data. If the important value is not in the JSON data, use the current important value of the task
    db.session.commit() # commit the session to the database
    return jsonify({'sucess': True, 'important': task.important}) # return a JSON response with the success status and the new important status of the task


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)