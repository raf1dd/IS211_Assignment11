"""
Script: todoapp.py
A simple Flask To-Do List application.
"""

from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Global list to store to-do items
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Basic Email Validation regex
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Validate email and priority
    if not email or not re.match(email_regex, email):
        return redirect(url_for('index'))
    
    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))

    if task:
        todos.append({
            'task': task,
            'email': email,
            'priority': priority
        })

    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    global todos
    todos = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
