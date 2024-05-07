from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Sample initial to-do list
todo_list = [{"task": "Learn Flask", "completed": False},
             {"task": "Build a simple web app", "completed": False},
             {"task": "Deploy to Heroku", "completed": False}]

@app.route('/')
def index():
    # Preprocess todo_list with indices
    todo_list_with_indices = [(index, todo) for index, todo in enumerate(todo_list)]
    return render_template('index.html', todo_list=todo_list_with_indices)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']
    if task:
        todo_list.append({"task": task, "completed": False})
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    del todo_list[index]
    return redirect(url_for('index'))

@app.route('/complete/<int:index>', methods=['POST'])
def complete_todo(index):
    todo_list[index]['completed'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)